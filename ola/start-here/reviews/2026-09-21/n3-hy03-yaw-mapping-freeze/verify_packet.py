"""Check the HY-03 packet against its own JSON. Does not invent results."""
import json
import sys
from pathlib import Path

from bridge_core import (
    FROZEN_CLAMP_DEG,
    FROZEN_GAIN_DEG,
    FROZEN_SIGN,
    FROZEN_WATCHDOG_S,
    HY03_LABEL,
    SIGN_NORMATIVE,
)

R = Path(__file__).resolve().parent


def load(name):
    return json.loads((R / name).read_text(encoding='utf-8'))


def main():
    required = [
        'INDEX.html', 'README.md', 'READY_FOR_OLA.md', 'DEFECT_REGISTER.md',
        'SOURCE_BRIEF.md', 'CRITICAL_OPEN.md', 'frozen_config.json', 'config_template.json',
        'config_unconfigured.json',
        'bridge_core.py', 'unit_verification.json', 'packet_verification.json',
        'camera_probe.json', 'gym_spotcheck.json', 'gym_samples.json',
    ]
    missing = [name for name in required if not (R / name).is_file()]
    if missing:
        print('MISSING', missing)
        return 1
    unit = load('unit_verification.json')
    gym = load('gym_spotcheck.json')
    camera = load('camera_probe.json')
    packet = load('packet_verification.json')
    frozen = load('frozen_config.json')
    template = load('config_template.json')
    unconfigured = load('config_unconfigured.json')
    problems = []
    if unit.get('status') != 'PASS' or unit.get('failures') != 0 or unit.get('errors') != 0:
        problems.append('unit verification is not a clean PASS')
    if unit.get('test_methods') != 6:
        problems.append('unit method count drifted')
    for name in ('sign', 'clamp', 'idle_home_zero', 'watchdog_stale'):
        if name not in unit.get('covered', []):
            problems.append('missing coverage ' + name)
    if frozen.get('label') != HY03_LABEL:
        problems.append('freeze label missing')
    if frozen.get('sign') != FROZEN_SIGN or frozen.get('gain_deg_per_signed_x') != FROZEN_GAIN_DEG:
        problems.append('frozen sign/gain drifted')
    if frozen.get('clamp_deg') != FROZEN_CLAMP_DEG or frozen.get('watchdog_s') != FROZEN_WATCHDOG_S:
        problems.append('frozen clamp/watchdog drifted')
    if frozen.get('idle_policy') != 'home_zero' or frozen.get('performance_claim') != 'NONE':
        problems.append('idle or performance claim drifted')
    if HY03_LABEL not in frozen.get('assumptions', '') or 'ASSUMPTION' not in frozen.get('assumptions', ''):
        problems.append('assumptions text missing the plain-sight label')
    if SIGN_NORMATIVE not in frozen.get('sign_convention', ''):
        problems.append('normative sign text missing')
    if template.get('gain_deg_per_signed_x') != FROZEN_GAIN_DEG or template.get('clamp_deg') is None:
        problems.append('freeze template must carry non-null Lead values')
    if unconfigured.get('gain_deg_per_signed_x') is not None or unconfigured.get('watchdog_s') is not None:
        problems.append('unconfigured nulls must stay null so chase stays denied')
    root = R.parents[2]
    for rel in (
        'docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md',
        'docs/engineering/ELIAS_HY03_YAW_MAPPING_SUPPORT.md',
    ):
        if not (root / rel).is_file():
            problems.append('missing cite ' + rel)
    if packet.get('unit_status') != unit.get('status') or packet.get('unit_failures') != 0:
        problems.append('packet verification does not match unit JSON')
    if packet.get('unit_test_methods') != unit.get('test_methods'):
        problems.append('packet method count does not match unit JSON')
    if packet.get('hy02_gym_status') != gym.get('status'):
        problems.append('packet gym status does not match gym JSON')
    if packet.get('open_critical') != ['B-06', 'C-01', 'SAF-02'] or packet.get('closed_critical') != []:
        problems.append('critical disposition drifted')
    if packet.get('track_a_proves_strike_impulse') or packet.get('po_usd') != 0:
        problems.append('strike or spend claim drifted')
    if camera.get('status') == 'SKIPPED_NO_CAMERA' and gym.get('status') != 'SKIPPED_NO_CAMERA':
        problems.append('missing camera must stay SKIPPED_NO_CAMERA')
    if gym.get('status') == 'CAMERA_PRESENT_NO_SINGLE_FACE' and gym.get('stills'):
        problems.append('no-face gym must not carry stills')
    if gym.get('film') is not None:
        problems.append('this grab must not claim a film')
    text = (R / 'READY_FOR_OLA.md').read_text(encoding='utf-8')
    if 'ASSUMPTION / DESIGN ESTIMATE' not in text or '## Plain-language glossary' not in text:
        problems.append('READY_FOR_OLA missing label or glossary')
    if problems:
        print('\n'.join(problems))
        return 1
    print(json.dumps(dict(status='PASS', unit=unit['status'], gym=gym['status'], camera=camera['status']), indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
