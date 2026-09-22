"""Burn ASSUMPTION HUDs and encode the teaching films.

Authored review rate is 12 fps. That number is the film clock, not a measured
camera, detector, or machine rate.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import cv2
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(r"C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag")
PKT = ROOT / "reviews" / "2026-09-21" / "n3-viz-pack-soft-phys-envelope-c01-saf"
MEDIA = PKT / "media"
YAW_PKT = ROOT / "reviews" / "2026-09-21" / "n3-head-yaw-live-usb-path"
MEDIA.mkdir(parents=True, exist_ok=True)

FONT = "C:/Windows/Fonts/segoeui.ttf"
BOLD = "C:/Windows/Fonts/segoeuib.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)


def encode(folder, count, dest, fps=12):
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg", "-y", "-framerate", str(fps), "-i", str(folder / "%04d.png"),
        "-frames:v", str(count), "-c:v", "libx264", "-crf", "20",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(dest),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    probe = json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-count_frames", "-show_streams", "-of", "json", str(dest),
    ]))
    stream = probe["streams"][0]
    frames = int(stream["nb_read_frames"])
    if frames != count:
        raise RuntimeError(f"{dest.name} decoded {frames} frames, expected {count}")
    return {
        "path": str(dest.relative_to(ROOT)).replace("\\", "/"),
        "decoded_frames": frames,
        "encoded_fps": stream["r_frame_rate"],
        "duration_s": stream["duration"],
        "resolution": [int(stream["width"]), int(stream["height"])],
        "fps_note": "Authored review rate only. Not a measured camera, detector, or machine rate.",
    }


def save_still(im, name):
    im.save(MEDIA / name)


def cyan_count(path):
    im = Image.open(path).convert("RGB")
    px = im.load()
    w, h = im.size
    n = 0
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            if g > 180 and b > 180 and r < 100 and (g + b - 2 * r) > 200:
                n += 1
    return n


def compose_cues():
    meta = json.loads((PKT / "raw" / "cue_phases.json").read_text(encoding="utf-8"))
    out = PKT / "raw" / "cue_hud"
    out.mkdir(parents=True, exist_ok=True)
    titles = {
        "rest": "REST",
        "swell": "SWELL  ·  common mode",
        "bend": "BEND  ·  U1 / F1 ahead of partner",
        "twist": "TWIST  ·  T1 ahead of T2",
        "return": "RETURN TO REST",
    }
    stills = {6: "cue_rest.png", 34: "cue_swell.png", 64: "cue_bend.png", 94: "cue_twist.png", 122: "cue_return.png"}
    count = int(meta["frames"])
    for frame in range(1, count + 1):
        phase = meta["phase_by_frame"][str(frame)]
        im = Image.new("RGB", (1500, 900), "#101c2a")
        d = ImageDraw.Draw(im)
        d.text((36, 18), "SOFT-PHYSICS CUE SHEET", font=font(32, True), fill="#e9f2fa")
        d.text((36, 58), titles.get(phase, phase), font=font(26, True), fill="#f4c982")
        shot = Image.open(PKT / "raw" / "cue" / f"{frame:04d}.png").convert("RGB")
        im.paste(shot, (260, 110))
        d = ImageDraw.Draw(im)
        lines = [
            "ASSUMPTION HUD — teaching shapes only. Twin is not System ID.",
            "p_norm is a teaching input in [0, 1]. ASSUMPTION. Not measured pressure.",
            "HYPOTHESIS, not a setpoint: paper section 6 maps p_norm = 1 to 40 kPa on the Ecoflex example.",
            "DESIGN ESTIMATE, not a coupon: Ecoflex E 0.118 MPa, Dragon Skin 30 E 1.02 MPa, ratio about 8.6x.",
            "DESIGN ASSUMPTION: textile lambda_max 1.10. Not measured strain. Glove 14 oz is an ASSUMPTION.",
            "Return is a DESIGN ESTIMATE order. Vent may dominate. Not a measured cycle. No cycle life.",
            "Critical B-06 OPEN. Critical C-01 OPEN. No spend. No physical actuation.",
        ]
        y = 690
        for i, line in enumerate(lines):
            d.text((36, y), line, font=font(18, i == 0), fill="#f4c982" if i == 0 else "#d5e0ea")
            y += 26
        im.save(out / f"{frame:04d}.png")
        if frame in stills:
            save_still(im, stills[frame])
    sheet = Image.new("RGB", (1500, 980), "#101c2a")
    for i, name in enumerate(["cue_rest.png", "cue_swell.png", "cue_bend.png", "cue_twist.png", "cue_return.png"]):
        tile = Image.open(MEDIA / name)
        tile.thumbnail((750, 450))
        sheet.paste(tile, ((i % 2) * 750, (i // 2) * 460))
    sheet.save(MEDIA / "cue_contact_sheet.png")
    info = encode(out, count, MEDIA / "soft_phys_cues_review.mp4")
    info["stills"] = list(stills.values()) + ["cue_contact_sheet.png"]
    info["label"] = "ASSUMPTION / DESIGN ESTIMATE / HYPOTHESIS. Not measured pressure, strain, force, or cycle life."
    return info


def compose_yaw():
    rows = json.loads((YAW_PKT / "udp_received.json").read_text(encoding="utf-8"))
    episode = [json.loads(x) for x in (YAW_PKT / "episode.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    if len(rows) != len(episode):
        raise RuntimeError(f"timeline length {len(rows)} != episode {len(episode)}")
    cap = cv2.VideoCapture(str(YAW_PKT / "media" / "input_synthetic.avi"))
    out = PKT / "raw" / "yaw_hud"
    out.mkdir(parents=True, exist_ok=True)
    titles = {
        "center": "CENTER / head prior enabled",
        "left": "HEAD MOVES LEFT / carrier follows",
        "right": "HEAD MOVES RIGHT / carrier follows",
        "absent_with_face": "PRESENCE ABSENT / idle despite face",
        "invalid_head_present": "HEAD INVALID / idle despite presence",
        "presence_fault": "PRESENCE FAULT / forced absent + idle",
        "stale_sync": "STALE SYNC / chase blocked",
        "inhibit": "INHIBIT LATCH / idle until manual reset",
        "e_stop": "SIMULATED E-STOP / chase blocked",
    }
    stills = {30: "yaw_slim_head_left.png", 68: "yaw_slim_head_right.png"}
    cyan = {}
    for r, p in zip(rows, episode):
        ok, frame = cap.read()
        if not ok:
            raise RuntimeError("synthetic clip ended early")
        twin_path = PKT / "raw" / "yaw" / f"{r['frame']:04d}.png"
        if not twin_path.exists():
            raise RuntimeError(f"missing yaw render {twin_path.name}")
        if r["frame"] in (30, 68):
            cyan[str(r["frame"])] = cyan_count(twin_path)
        outp = r["output"]
        im = Image.new("RGB", (1500, 900), "#101c2a")
        d = ImageDraw.Draw(im)
        d.text((35, 16), "HEAD TO CARRIER YAW  ·  SLIM LEFT ROOT", font=font(30, True), fill="#e9f2fa")
        d.text((36, 54), "I1_bag_black collars. Cyan pads retired. Re-encode of the slimmed twin.", font=font(18), fill="#9ab3c9")
        d.text((36, 84), titles[r["stimulus"]], font=font(24, True), fill="#78e9cc" if outp["effective_enable"] else "#ffc775")
        pic = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        im.paste(pic, (35, 130))
        twin = Image.open(twin_path).convert("RGB")
        im.paste(twin, (700, 125))
        d = ImageDraw.Draw(im)
        cx = "invalid" if p["head_centroid_x"] is None else f"{p['head_centroid_x']:.3f}"
        d.text((36, 520), f"Head centroid x: {cx}    presence: {'YES' if outp['user_present'] else 'NO'}    head valid: {'YES' if p['head_hypothesis_valid'] else 'NO'}", font=font(20), fill="#bfd0df")
        d.text((36, 555), f"Effective yaw: {outp['yaw_cmd']:+.2f} deg    {'FOLLOW' if outp['effective_enable'] else 'HOME / IDLE'}", font=font(24, True), fill="#78e9cc" if outp["effective_enable"] else "#ffc775")
        d.text((36, 600), "ASSUMPTION HUD — demo mapping only. Gain, clamp, idle, and timing remain TBD — Lead.", font=font(20), fill="#f4c982")
        d.text((36, 632), "Left-root slim is a visual alignment, not a measured section. Right collar was not edited.", font=font(20), fill="#f4c982")
        d.text((36, 664), "Prescribed twin motion. Not measured force, camera accuracy, or punch power.", font=font(20), fill="#d5e0ea")
        d.text((36, 700), "Yaw degrees on this card are the digital command, not a measured joint.", font=font(20), fill="#d5e0ea")
        d.text((36, 748), "B-06 Critical OPEN. C-01 Critical OPEN. SAF-02 stays OPEN. No physical actuation. No spend.", font=font(20), fill="#ffc7b8")
        d.text((36, 790), "12 fps is the authored review clock, not a measured detector rate. Synthetic clip, not live-gym proof.", font=font(18), fill="#9ab3c9")
        im.save(out / f"{r['frame']:04d}.png")
        if r["frame"] in stills:
            save_still(im, stills[r["frame"]])
    cap.release()
    if any(cyan.values()):
        raise RuntimeError(f"bright-cyan pixels present in slim yaw renders: {cyan}")
    info = encode(out, len(rows), MEDIA / "head_yaw_review_slim_root.mp4")
    yaw_copy = YAW_PKT / "media" / "head_yaw_review_slim_root.mp4"
    shutil.copy2(MEDIA / "head_yaw_review_slim_root.mp4", yaw_copy)
    info["yaw_packet_copy"] = str(yaw_copy.relative_to(ROOT)).replace("\\", "/")
    info["bright_cyan_pixels_frames_30_and_68"] = cyan
    info["cyan_rule"] = "G>180, B>180, R<100, G+B-2R>200 on the twin render, not the composite."
    info["label"] = "ASSUMPTION visual. I1_bag_black. Cyan pads retired. Not a measured section."
    (PKT / "raw" / "yaw_cyan_audit.json").write_text(json.dumps(cyan, indent=2), encoding="utf-8")
    return info


def banner(src_folder, count, dest_name, stills, footer_lines, still_frames):
    out = PKT / "raw" / (dest_name + "_hud")
    out.mkdir(parents=True, exist_ok=True)
    for frame in range(1, count + 1):
        shot = Image.open(src_folder / f"{frame:04d}.png").convert("RGB")
        im = Image.new("RGB", (1500, 900), "#101c2a")
        im.paste(shot, (0, 0))
        d = ImageDraw.Draw(im)
        d.rectangle((0, 820, 1500, 900), fill="#101c2a")
        y = 828
        for i, line in enumerate(footer_lines):
            d.text((24, y), line, font=font(16, i == 0), fill="#f4c982" if i == 0 else "#d5e0ea")
            y += 22
        im.save(out / f"{frame:04d}.png")
        if frame in still_frames:
            save_still(im, still_frames[frame])
    info = encode(out, count, MEDIA / dest_name)
    info["stills"] = list(stills)
    return info


def compose_b06():
    return banner(
        PKT / "raw" / "b06",
        96,
        "b06_envelope_keepout_review.mp4",
        ["b06_stack.png", "b06_pitch_lock.png", "b06_flex_loops.png", "b06_pinch.png"],
        [
            "ASSUMPTION HUD — block envelopes are drawing aids. Not measured clearance. No invented millimeters.",
            "Critical B-06 stays OPEN. pitch_lock_engaged is the only normative lock bit. Chafe sleeve stays unfrozen. No PO.",
        ],
        {8: "b06_stack.png", 32: "b06_pitch_lock.png", 64: "b06_flex_loops.png", 80: "b06_pinch.png"},
    )


def compose_c01():
    return banner(
        PKT / "raw" / "c01",
        96,
        "c01_coupon_geometry_review.mp4",
        ["c01_tb01.png", "c01_tb02u.png", "c01_tb02f.png", "c01_later.png"],
        [
            "ASSUMPTION HUD — coupon board only. No cast. No mold. Critical C-01 stays OPEN. Not System ID.",
            "Planning lengths in the index are paper ASSUMPTIONS, not product free lengths and not measured strain.",
        ],
        {8: "c01_tb01.png", 24: "c01_tb02u.png", 40: "c01_tb02f.png", 88: "c01_later.png"},
    )


def lamp(d, xy, on, label, sub):
    x, y = xy
    fill = "#1f8f62" if on else "#3a4654"
    edge = "#78e9cc" if on else "#6d7c8d"
    d.rounded_rectangle((x, y, x + 280, y + 92), radius=8, fill=fill, outline=edge, width=3)
    d.text((x + 16, y + 14), label, font=font(20, True), fill="#f4f7fb")
    d.text((x + 16, y + 48), sub, font=font(16), fill="#d5e0ea")


def compose_saf():
    """Digital schematic only. No mechanism, no valve, no physical actuation."""
    out = PKT / "raw" / "saf_hud"
    out.mkdir(parents=True, exist_ok=True)
    count = 108
    # Chapters of 18 frames: intro, happy, absent, fault, latch/limp, reset.
    chapters = ["intro", "happy", "absent", "fault", "limp", "reset"]
    stills = {9: "saf_equation.png", 27: "saf_happy.png", 45: "saf_absent.png", 63: "saf_fault.png", 81: "saf_limp.png", 99: "saf_reset.png"}
    for frame in range(1, count + 1):
        chapter = chapters[min(len(chapters) - 1, (frame - 1) // 18)]
        present = chapter == "happy"
        head = chapter in ("happy", "absent", "limp", "reset")
        fault = chapter == "fault"
        latched = chapter in ("limp", "reset")
        estop = chapter == "limp"
        if fault:
            present = False
        session = present and head and not latched
        yaw_enable = session and not estop
        im = Image.new("RGB", (1500, 900), "#101c2a")
        d = ImageDraw.Draw(im)
        d.text((36, 20), "SAF-02 / P-05  ·  DIGITAL HIL SCHEMATIC", font=font(30, True), fill="#e9f2fa")
        d.text((36, 62), "Illustration only. session_enable does not authorize physical actuation or a pressurized strike.", font=font(18), fill="#f4c982")
        d.text((36, 100), "session_enable = user_present AND head_hypothesis_valid AND NOT inhibit_latched", font=font(22, True), fill="#78e9cc")
        d.text((36, 136), "Tag on this film: SIMULATED_BOOL_NOT_HARDWARE. ToF preferred later. Mat omitted for MVP.", font=font(18), fill="#9ab3c9")
        lamp(d, (40, 190), present, "user_present", "YES" if present else "ABSENT / fail-safe")
        lamp(d, (360, 190), head, "head_hypothesis_valid", "YES" if head else "INVALID")
        lamp(d, (680, 190), latched, "inhibit_latched", "LATCHED" if latched else "clear")
        lamp(d, (1000, 190), estop, "e_stop_asserted", "ASSERTED" if estop else "clear (sim)")
        d.line((180, 282, 180, 340, 750, 340), fill="#78e9cc", width=3)
        d.line((500, 282, 500, 320, 750, 320), fill="#78e9cc", width=3)
        d.line((820, 282, 820, 300, 750, 300), fill="#ffb4a8", width=3)
        lamp(d, (610, 360), session, "session_enable", "TRUE — digital only" if session else "FALSE")
        lamp(d, (960, 360), yaw_enable, "yaw_cmd_enable", "pass yaw_cmd" if yaw_enable else "idle / home_zero")
        stories = {
            "intro": "Chapter: equation. Presence, head, and a clear latch are all required. Any false term keeps the session off.",
            "happy": "Chapter: present + valid head + clear latch. Digital session / logging may enable. This is still not S3 motion.",
            "absent": "Chapter: head without presence. Session stays false. No yaw chase toward empty space. Presence hard-interlocks strike.",
            "fault": "Chapter: presence_sensor_fault forces user_present false. Treat as absent. Idle / safe.",
            "limp": "Chapter: E-stop sim ORs into the latch. Supply story is inhibit + Lead-approved vent. No psi on this film. P-05 stays OPEN.",
            "reset": "Chapter: manual reset is separate from arm. AI restart does not clear the latch. Reset does not start motion.",
        }
        d.rounded_rectangle((40, 500, 1460, 620), radius=8, fill="#18283a", outline="#38566c", width=2)
        d.text((60, 520), stories[chapter], font=font(22, True), fill="#e9f2fa")
        d.text((60, 565), "Limp / vent on this card is a narrative arrow, not a valve command and not a measured droop.", font=font(18), fill="#d5e0ea")
        d.text((40, 650), "Fail-safe absent: sensor fault, loss, or power loss sets user_present false. AI must not force present.", font=font(18), fill="#d5e0ea")
        d.text((40, 682), "Twin digital watchdog_s = 2.0 is a Lead Track A freeze. NOT a measured latency bar or hardware limit.", font=font(18), fill="#f4c982")
        d.text((40, 730), "SAF-02 Critical OPEN. P-05 Critical OPEN. Topology, PL/SIL, stop time, force, and pressure stay Lead TBD.", font=font(20, True), fill="#ffc7b8")
        d.text((40, 770), "No invented PL, SIL, milliseconds, psi, or newtons. No physical actuation. No spend.", font=font(20), fill="#ffc7b8")
        d.text((40, 830), "12 fps authored review clock only. Digital HIL stub. Not a hardware acceptance test.", font=font(18), fill="#9ab3c9")
        im.save(out / f"{frame:04d}.png")
        if frame in stills:
            save_still(im, stills[frame])
    info = encode(out, count, MEDIA / "saf02_presence_inhibit_hil_review.mp4")
    info["stills"] = list(stills.values())
    info["label"] = "Illustration only. SIMULATED_BOOL_NOT_HARDWARE. SAF-02 and P-05 stay OPEN."
    return info


def main():
    which = set(sys.argv[1:] or ["all"])
    if "all" in which:
        which = {"cue", "yaw", "b06", "c01", "saf"}
    report = {}
    if "saf" in which:
        report["saf"] = compose_saf()
        print("SAF_COMPOSED", flush=True)
    if "cue" in which:
        report["cue"] = compose_cues()
        print("CUE_COMPOSED", flush=True)
    if "yaw" in which:
        report["yaw"] = compose_yaw()
        print("YAW_COMPOSED", flush=True)
    if "b06" in which:
        report["b06"] = compose_b06()
        print("B06_COMPOSED", flush=True)
    if "c01" in which:
        report["c01"] = compose_c01()
        print("C01_COMPOSED", flush=True)
    path = PKT / "raw" / "compose_report.json"
    prior = {}
    if path.exists():
        prior = json.loads(path.read_text(encoding="utf-8"))
    prior.update(report)
    path.write_text(json.dumps(prior, indent=2), encoding="utf-8")
    print("COMPOSE_DONE", ",".join(sorted(report)), flush=True)


if __name__ == "__main__":
    main()
