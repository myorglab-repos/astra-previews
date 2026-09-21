"""Replay the synthetic clip over actual loopback UDP. Receiver re-derives enable/yaw.

Does not remake the ACCEPTED-A Blender successor. Software-path proof only.
"""
import json
import socket
import subprocess
import sys
import time
from pathlib import Path

from bridge_core import ReceiverState

R = Path(__file__).resolve().parent
CFG = json.loads((R / 'demo_config.json').read_text(encoding='utf-8-sig'))


def main():
    episode = R / 'episode.jsonl'
    if episode.exists():
        episode.unlink()
    state = ReceiverState(CFG)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((CFG['host'], CFG['port']))
    sock.settimeout(30)
    cmd = [
        sys.executable,
        str(R / 'capture_head.py'),
        '--clip', str(R / 'media' / 'input_synthetic.avi'),
        '--timeline', str(R / 'presence_timeline.json'),
        '--config', str(R / 'demo_config.json'),
        '--head-spotcheck-approved',
        '--send',
        '--wait-ack',
        '--log', str(episode),
    ]
    log = (R / 'clip_integration.log').open('w', encoding='utf-8')
    process = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)
    received = []
    try:
        for frame in range(1, 145):
            raw, addr = sock.recvfrom(65535)
            packet, out = state.ingest(raw)
            if packet is None:
                raise RuntimeError('Rejected detector packet: ' + str(out))
            if packet['seq'] != frame - 1:
                raise RuntimeError(f'Unexpected seq {packet["seq"]} at frame {frame}')
            # Sender-computed yaw/enable are ignored; only receiver output is recorded.
            received.append(dict(
                frame=frame,
                seq=packet['seq'],
                stimulus=packet.get('stimulus'),
                head_centroid_x=packet['head_centroid_x'],
                sender_yaw_ignored=packet.get('yaw_cmd'),
                output=out,
                carrier_yaw_deg=out['yaw_cmd'],
            ))
            sock.sendto(json.dumps(dict(seq=packet['seq'], accepted=True)).encode(), addr)
        raw, addr = sock.recvfrom(65535)
        packet, out = state.ingest(raw)
        if not packet or out['effective_enable'] or out['yaw_cmd'] != 0:
            raise RuntimeError('EOF did not idle')
        if process.wait(timeout=30) != 0:
            raise RuntimeError('capture_head exited non-zero')
    finally:
        sock.close()
        log.close()
        if process.poll() is None:
            process.kill()
            process.wait()
    if len(received) != 144:
        raise RuntimeError(f'expected 144 packets, got {len(received)}')
    left = received[29]['output']['yaw_cmd']
    right = received[67]['output']['yaw_cmd']
    if not (left < 0 < right):
        raise RuntimeError(f'direction failed: left={left} right={right}')
    for row in received[72:]:
        if row['output']['yaw_cmd'] != 0 or row['output']['effective_enable']:
            raise RuntimeError('idle chapter did not home-zero')
    (R / 'udp_received.json').write_text(json.dumps(received, indent=2), encoding='utf-8')
    (R / 'integration_verification.json').write_text(json.dumps(dict(
        status='PASS',
        transport='actual loopback UDP/JSON',
        detector='OpenCV Haar',
        packets_applied=len(received),
        EOF_idle=True,
        receiver_rederived=True,
        sender_yaw_trusted=False,
        blender_successor_remade=False,
        parent_packet='reviews/2026-09-21/n3-head-track-yaw-bridge',
        sender_command=cmd,
        performance_claim='NONE; per-frame acknowledgements pace offline integration, not a real-time benchmark',
    ), indent=2), encoding='utf-8')
    print('CLIP_INTEGRATION_PASS', len(received), 'packets; left', left, 'right', right)


if __name__ == '__main__':
    main()
