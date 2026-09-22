"""Teaching boards for the physics-overlay / board-refresh viz pack.

12 fps is the authored review clock. It is not a measured camera, detector,
or machine rate. Cards are illustrations. They do not close Criticals.
Twin overlays are not System ID.
"""
from __future__ import annotations

import json
import math
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[4]
PKT = Path(__file__).resolve().parents[1]
MEDIA = PKT / "media"
RAW = PKT / "raw"

W, H = 1500, 900
BG = (16, 28, 42)
PANEL = (24, 40, 58)
LINE = (44, 67, 88)
GOLD = (244, 201, 130)
TEXT = (232, 238, 245)
MUTED = (183, 198, 212)
RED = (224, 122, 122)
GREEN = (157, 202, 168)
AMBER = (226, 177, 90)
TEAL = (142, 200, 196)
ROSE = (214, 146, 156)
WHITE = (249, 245, 239)

FONT = "C:/Windows/Fonts/segoeui.ttf"
BOLD = "C:/Windows/Fonts/segoeuib.ttf"

SPOKEN: list[str] = []


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)


F15 = font(15)
F15B = font(15, True)
F16 = font(16)
F16B = font(16, True)
F18 = font(18)
F18B = font(18, True)
F20B = font(20, True)
F22 = font(22)
F22B = font(22, True)
F28B = font(28, True)
F34B = font(34, True)


def say(d, xy, text, fnt, fill):
    SPOKEN.append(text)
    d.text(xy, text, font=fnt, fill=fill)


def wrap(draw, text, fnt, width):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines or [""]


def new_card(kicker, title, badge, badge_fill):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 8), fill=(166, 48, 53))
    say(d, (36, 22), kicker, F16B, GOLD)
    say(d, (36, 48), title, F34B, TEXT)
    if badge:
        bw = d.textlength(badge, font=F16B) + 28
        x0 = W - 36 - bw
        d.rounded_rectangle((x0, 22, x0 + bw, 52), radius=8, fill=badge_fill)
        say(d, (x0 + 14, 28), badge, F16B, BG)
        SPOKEN.append(badge)
    SPOKEN.append(kicker)
    SPOKEN.append(title)
    return im, d


def footer(d, lines):
    d.rectangle((0, 768, W, H), fill=(12, 22, 34))
    d.rectangle((0, 768, W, 772), fill=GOLD)
    y = 784
    for i, line in enumerate(lines[:4]):
        say(d, (36, y), line, F16B if i == 0 else F16, GOLD if i == 0 else MUTED)
        y += 24


def panel(d, box, title, body_lines, title_fill=GOLD):
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, radius=12, fill=PANEL, outline=LINE, width=2)
    say(d, (x0 + 18, y0 + 14), title, F20B, title_fill)
    y = y0 + 52
    max_w = (x1 - x0) - 36
    for line in body_lines:
        for wl in wrap(d, line, F18, max_w):
            if y > y1 - 28:
                return
            say(d, (x0 + 18, y), wl, F18, TEXT)
            y += 26


def bullets(d, x, y, items, width, fnt=F22, fill=TEXT, gap=8):
    for item in items:
        lines = wrap(d, item, fnt, width - 28)
        d.ellipse((x, y + 8, x + 10, y + 18), fill=GOLD)
        for wl in lines:
            say(d, (x + 22, y), wl, fnt, fill)
            y += 28
        y += gap
    return y


def save_frame(folder, im, n):
    im.save(folder / f"{n:04d}.png")


def encode(folder, count, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg", "-y", "-framerate", "12", "-i", str(folder / "%04d.png"),
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
    if stream["r_frame_rate"] != "12/1":
        raise RuntimeError(f"{dest.name} clock {stream['r_frame_rate']}, expected 12/1")
    return {
        "path": str(dest.relative_to(ROOT)).replace("\\", "/"),
        "decoded_frames": frames,
        "encoded_fps": stream["r_frame_rate"],
        "duration_s": stream["duration"],
        "resolution": [int(stream["width"]), int(stream["height"])],
        "fps_note": "Authored review clock only. Not a measured camera, detector, or machine rate.",
    }


def hold(folder, stills, start, count, painter, still_name):
    im = None
    for i in range(count):
        im = painter()
        save_frame(folder, im, start + i)
    if still_name and im is not None:
        im.save(MEDIA / still_name)
        stills.append(still_name)
    return start + count


def fresh(folder):
    if folder.exists():
        for p in folder.glob("*.png"):
            p.unlink()
    folder.mkdir(parents=True, exist_ok=True)


def clock_foot():
    return [
        "ASSUMPTION / DESIGN ESTIMATE / HYPOTHESIS in plain sight. Twin is not System ID.",
        "12 fps authored review clock. Not a measured camera, detector, or machine rate.",
        "paper only / Critical OPEN.",
    ]


def film_a(report):
    folder = RAW / "a_soft"
    fresh(folder)
    stills = []
    n = 1
    foot = [
        "ASSUMPTION HUD. Cite ACCEPTED-A Soft physics. mu, lambda_max, glove, and p_norm are not lab results.",
        "Twin is not System ID. 12 fps authored review clock. Not a measured detector rate.",
        "paper only / Critical OPEN. C-01 stays OPEN. B-06 stays OPEN.",
    ]

    def title():
        im, d = new_card(
            "A  ·  SOFT PHYSICS OVERLAY",
            "Neo-Hookean, then p_norm to bend",
            "ASSUMPTION HUD",
            AMBER,
        )
        bullets(d, 48, 140, [
            "Cue-sheet HUD. Not a re-render of the yaw twin. Not a measured pressure trace.",
            "ACCEPTED-A Soft physics: Ecoflex 00-30 shear modulus mu about 39.4 kPa. DESIGN ESTIMATE from the TDS 100% modulus bridge.",
            "Textile lambda_max 1.10. DESIGN ASSUMPTION. Glove mass 14 oz. ASSUMPTION.",
            "Sequence on the next card: p_norm from rest, to swell, to bend. The 40 kPa map is a HYPOTHESIS.",
            "Tip-force rows in the paper stay HYPOTHESIS order-of-magnitude. They are not drawn as a result.",
        ], 1380, F22)
        footer(d, foot)
        return im

    def mu_card():
        im, d = new_card(
            "A  ·  NEO-HOOKEAN BRIDGE",
            "TDS modulus to shear modulus",
            "DESIGN ESTIMATE",
            GOLD,
        )
        panel(d, (48, 130, 720, 730), "Ecoflex 00-30  ·  headline", [
            "100% modulus 10 psi on an unconstrained coupon. ASSUMPTION bridge, not a sleeved fit.",
            "At lambda = 2: C1 = sigma / 3.5, mu = 2 C1.",
            "mu about 39.4 kPa (39.399 kPa in the table).",
            "E about 0.118 MPa. DESIGN ESTIMATE.",
            "Specific gravity 1.07 g/cc. TDS.",
            "Primary cast class in the paper. Not a weighed part.",
        ], TEAL)
        panel(d, (760, 130, 1452, 730), "Comparatives  ·  same bridge", [
            "Dragon Skin 10 mu about 86.7 kPa. DESIGN ESTIMATE.",
            "Dragon Skin 20 mu about 193 kPa. DESIGN ESTIMATE.",
            "Dragon Skin 30 mu about 339 kPa. E about 1.02 MPa. ACCEPTED-A comparative.",
            "Stiffness rank DS30 / Ecoflex about 8.6 times. DESIGN ESTIMATE.",
            "Not a coupon result. C-01 stays OPEN.",
            "Twin morph is not identification.",
        ], GOLD)
        footer(d, foot)
        return im

    def overlay(p):
        im, d = new_card(
            "A  ·  CUE SHEET",
            "p_norm  to  swell  to  bend",
            "NOT SYSTEM ID",
            RED,
        )
        d.rounded_rectangle((48, 128, 980, 730), radius=14, fill=PANEL, outline=LINE, width=2)
        say(d, (70, 142), "CUE SHEET  ·  one arm, side view  ·  drawing", F16B, GOLD)
        swell = 1.0 + 0.38 * min(1.0, p / 0.38)
        bend = max(0.0, (p - 0.34) / 0.66) * 42.0
        if p < 0.12:
            phase = "REST"
        elif p < 0.42:
            phase = "SWELL"
        else:
            phase = "BEND"
        ox, oy = 150, 340
        uh, uw = int(70 * swell), 260
        d.rounded_rectangle((ox, oy - uh // 2, ox + uw, oy + uh // 2), radius=30, fill=ROSE)
        for i in range(3):
            cx = ox + 70 + i * 80
            rw, rh = int(22 * swell), int(16 * swell)
            d.ellipse((cx - rw, oy - rh, cx + rw, oy + rh), fill=TEAL)
        ang = math.radians(-bend)
        fx, fy = ox + uw - 8, oy
        fl, fh = 180, int(56 * swell)
        poly = []
        for px, py in ((0, -fh / 2), (fl, -fh / 2), (fl, fh / 2), (0, fh / 2)):
            poly.append((fx + px * math.cos(ang) - py * math.sin(ang), fy + px * math.sin(ang) + py * math.cos(ang)))
        d.polygon(poly, fill=ROSE)
        for i in range(3):
            along = 55 + i * 70
            cx = fx + along * math.cos(ang)
            cy = fy + along * math.sin(ang)
            rw, rh = int(18 * swell), int(12 * swell)
            d.ellipse((cx - rw, cy - rh, cx + rw, cy + rh), fill=TEAL)
        d.rectangle((64, 600, 964, 714), fill=(18, 32, 46))
        say(d, (78, 612), f"phase  {phase}", F22B, WHITE)
        say(d, (300, 612), f"p_norm  {p:.2f}", F22B, TEAL)
        say(d, (78, 648), "HYPOTHESIS map at 1.00 → 40 kPa Ecoflex-class. Not a gauge.", F16, MUTED)
        say(d, (78, 678), "Chambers are U / F teaching marks. Not measured strain.", F16, MUTED)
        d.rounded_rectangle((1004, 128, 1452, 730), radius=14, fill=(18, 32, 46), outline=GOLD, width=2)
        say(d, (1024, 146), "ASSUMPTION HUD", F20B, GOLD)
        say(d, (1024, 176), "DESIGN ESTIMATE / twin ≠ ID", F15B, AMBER)
        rows = [
            ("mu Ecoflex", "≈ 39.4 kPa", "DESIGN ESTIMATE"),
            ("lambda_max", "1.10", "DESIGN ASSUMPTION"),
            ("glove", "14 oz", "ASSUMPTION"),
            ("p_norm", f"{p:.2f}  in [0, 1]", "teaching input"),
            ("map at 1", "40 kPa class", "HYPOTHESIS"),
        ]
        y = 210
        for label, value, tag in rows:
            say(d, (1024, y), label, F16, MUTED)
            say(d, (1024, y + 22), value, F22B, TEXT)
            say(d, (1024, y + 52), tag, F15B, AMBER)
            y += 90
        footer(d, foot)
        return im

    def drivers():
        im, d = new_card(
            "A  ·  DRIVER MAP",
            "Named props are proposals, not a live file",
            "LEAD-CONFIRM",
            GOLD,
        )
        panel(d, (48, 130, 720, 730), "Custom properties  ·  ASSUMPTION", [
            "p_norm_U1 through p_norm_T2 drive the chamber morph. Rest is 0.",
            "mat_class 0 is Ecoflex. mat_class 1 is Dragon Skin 30. HUD rows swap only.",
            "dp_map_kPa is 40 or 100. HYPOTHESIS. Not a working pressure.",
            "lambda_max stays 1.10. DESIGN ASSUMPTION.",
            "m_glove_kg is 0.397, the 14 oz ASSUMPTION.",
            "hud_stamp stays: DESIGN ESTIMATE / twin is not System ID.",
            "Soft stays idle on the live blend. These names are not a schema freeze.",
        ], TEAL)
        panel(d, (760, 130, 1452, 730), "Shape keys  ·  ASSUMPTION", [
            "SK_BEND_UPPER follows a difference across U1–U3.",
            "SK_BEND_FOREARM follows a difference across F1–F3.",
            "SK_TWIST_WRIST follows opposite T1 and T2. No distal metal.",
            "SK_AXIAL_COMMON clamps at lambda_max.",
            "SK_REST_RETURN follows SO_VENT_STATE and tau_return_s. Not cycle life.",
            "Optional stiffness rank is about 8.6 times. DESIGN ESTIMATE. Not continuum FEA.",
            "C-01 stays OPEN. B-06 stays OPEN. paper only / Critical OPEN.",
        ], GOLD)
        footer(d, foot)
        return im

    def clamp():
        im, d = new_card(
            "A  ·  CLAMP AND NON-CLAIM",
            "Fiber limit, then stop",
            "NOT A LAB",
            RED,
        )
        panel(d, (48, 130, 720, 730), "What the overlay is allowed to say", [
            "lambda_max 1.10 is the planning textile clamp. DESIGN ASSUMPTION.",
            "Sensitivity band in the paper is 1.05 / 1.10 / 1.15. Not measured strain.",
            "Glove 14 oz = 0.397 kg baseline. ASSUMPTION. Band 12–16 oz stays in the paper.",
            "Bare Ecoflex stretch in the hoop idealization can sit outside that clamp.",
            "Useful axial strain on a sleeved wall is the fiber limit, about 0.10.",
            "Bend on the cue is differential chamber pressure, drawn, not identified.",
        ], TEAL)
        panel(d, (760, 130, 1452, 730), "What it does not say", [
            "Not System ID. Not a Track C force result.",
            "Not cycle life. Not a product working pressure.",
            "p_norm is not a gauge reading.",
            "The yaw twin was not re-saved for this card.",
            "C-01 stays Critical OPEN.",
            "B-06 stays Critical OPEN. paper only / Critical OPEN.",
        ], RED)
        footer(d, foot)
        return im

    n = hold(folder, stills, n, 24, title, "soft_phys_title.png")
    n = hold(folder, stills, n, 36, mu_card, "soft_phys_mu.png")
    frames_anim = 72
    mid = None
    for i in range(frames_anim):
        p = i / (frames_anim - 1)
        im = overlay(p)
        save_frame(folder, im, n + i)
        if i == 24:
            im.save(MEDIA / "soft_phys_swell.png")
            stills.append("soft_phys_swell.png")
        if i == frames_anim - 1:
            mid = im
    if mid is not None:
        mid.save(MEDIA / "soft_phys_bend.png")
        stills.append("soft_phys_bend.png")
    n += frames_anim
    n = hold(folder, stills, n, 36, drivers, "soft_phys_drivers.png")
    n = hold(folder, stills, n, 30, clamp, "soft_phys_clamp.png")
    info = encode(folder, n - 1, MEDIA / "soft_phys_neohook_overlay_review.mp4")
    info["stills"] = stills
    info["label"] = "Cue-sheet HUD. Neo-Hookean mu and p_norm to bend. Not System ID."
    report["films"]["A_soft_phys"] = info


def film_b(report):
    folder = RAW / "b_vent"
    fresh(folder)
    stills = []
    n = 1
    foot = [
        "DESIGN ESTIMATE time-order. Not cycle life. Not a measured return trace.",
        "Twin is not System ID. 12 fps authored review clock is not tau.",
        "paper only / Critical OPEN. TB-04 history is not in hand. C-01 stays OPEN.",
    ]

    def title():
        im, d = new_card(
            "B  ·  VENT VS ELASTIC RETURN",
            "Two clocks after a vent command",
            "NOT CYCLE LIFE",
            AMBER,
        )
        bullets(d, 48, 150, [
            "Source: soft return / vent time-order paper, beside ACCEPTED-A physics section 4.4.",
            "tau_el is elastic snapback after pressure is already gone. DESIGN ESTIMATE.",
            "tau_vent is orifice discharge of an ASSUMPTION lumen. Often longer.",
            "Planning return is at least the longer of the two. Typically seconds on the small-orifice rows.",
            "A limp bladder does not pull. Return work is elastomer, textile, and return bands.",
        ], 1380, F22)
        footer(d, foot)
        return im

    def timeline(t):
        im, d = new_card(
            "B  ·  TIME-ORDER DRAWING",
            "Elastic hundreds of ms, vent in seconds",
            "DRAWING AID",
            GOLD,
        )
        say(d, (48, 130), "Axis is a DESIGN ESTIMATE sketch from 0 to 6 s. Not a scope capture. Not the film clock.", F18, MUTED)
        x0, x1, y_el, y_v = 80, 1420, 250, 430
        d.line((x0, 620, x1, 620), fill=LINE, width=3)
        for s in range(0, 7):
            x = x0 + (x1 - x0) * (s / 6.0)
            d.line((x, 612, x, 632), fill=GOLD, width=2)
            say(d, (x - 10, 640), f"{s} s", F16, MUTED)
        # elastic marker ~0.7 s mean of 0.61–0.81
        el_x = x0 + (x1 - x0) * (0.71 / 6.0)
        d.rounded_rectangle((x0, y_el, el_x, y_el + 70), radius=8, fill=TEAL)
        say(d, (x0, y_el - 32), "tau_el   Ecoflex  ·  14 oz  ·  about 0.6–0.8 s", F18B, TEAL)
        say(d, (el_x + 16, y_el + 22), "DESIGN ESTIMATE", F16B, TEAL)
        # vent band 2.1 to 4.7, draw growing
        v0 = x0 + (x1 - x0) * (2.1 / 6.0)
        v1 = x0 + (x1 - x0) * (4.7 / 6.0)
        shown = v0 + (v1 - v0) * t
        d.rounded_rectangle((v0, y_v, max(shown, v0 + 8), y_v + 70), radius=8, fill=AMBER)
        say(d, (x0, y_v - 32), "tau_vent   1.0–1.5 mm orifice ASSUMPTION  ·  about 2–5 s", F18B, AMBER)
        tag_x = min(shown + 16, 1240)
        say(d, (tag_x, y_v + 22), "DESIGN ESTIMATE", F16B, AMBER)
        say(d, (80, 700), "Vent-dominated on these rows. Contested if the vent path is large — measure later. Not cycle life.", F18, TEXT)
        footer(d, foot)
        return im

    def numbers():
        im, d = new_card(
            "B  ·  LABELED ROWS",
            "ASSUMPTION inputs beside the clocks",
            "ASSUMPTION",
            AMBER,
        )
        panel(d, (48, 130, 720, 730), "Elastic  ·  DESIGN ESTIMATE", [
            "tau_el ~ square root of m / k_eff. Pressure already gone.",
            "Ecoflex, eta 0.20, 14 oz: about 810 ms.",
            "Ecoflex, eta 0.35, 14 oz: about 610 ms.",
            "Dragon Skin 30, 14 oz: about 210–275 ms.",
            "Glove 14 oz = 0.397 kg. ASSUMPTION.",
            "Section length 0.720 m and radius class 45 mm. ASSUMPTION.",
        ], TEAL)
        panel(d, (760, 130, 1452, 730), "Vent  ·  DESIGN ESTIMATE", [
            "TB-01 mid lumen 0.565 L. ASSUMPTION geometry.",
            "Orifice 1.0 mm: about 4.7 s for one volume.",
            "Orifice 1.5 mm: about 2.1 s for one volume.",
            "Longer tube: about 2–10 s planning band. HYPOTHESIS.",
            "Cd 0.60, air density 1.2 kg/m3, delta-P 40 kPa map. ASSUMPTION / HYPOTHESIS.",
            "Tube friction and return-band dissipation are not a measured history.",
        ], AMBER)
        footer(d, foot)
        return im

    def beats():
        im, d = new_card(
            "B  ·  STORYBOARD BEATS",
            "From the vent paper, not a new clock",
            "NOT CYCLE LIFE",
            AMBER,
        )
        panel(d, (48, 130, 720, 730), "B0 – B4", [
            "B0  Title. DESIGN ESTIMATE pedagogy.",
            "B1  Rest. U1–U3, F1–F3, T1–T2. Stored strain, not suction.",
            "B2  Inflate. p_norm map. HYPOTHESIS 40 kPa at 1.",
            "B3  Hold. Tip angle is a DESIGN ESTIMATE. Not System ID.",
            "B4  SO_VENT_STATE. Pressure leaving. Teaching t = 0.",
        ], TEAL)
        panel(d, (760, 130, 1452, 730), "B5 – B9", [
            "B5  Elastic ghost. tau_el about 0.6–0.8 s. DESIGN ESTIMATE.",
            "B6  Primary return is vent-limited. About 2–5 s. ASSUMPTION.",
            "B7  Planning return uses the longer clock. Vent often dominates.",
            "B8  A limp bladder cannot pull. Elastomer, textile, return bands.",
            "B9  Recalibrate when a coupon history exists. Not cycle life. C-01 stays OPEN.",
            "Soft stays idle on the live blend. paper only / Critical OPEN.",
        ], AMBER)
        footer(d, foot)
        return im

    def takeaway():
        im, d = new_card(
            "B  ·  PLANNING RULE",
            "Use the longer clock until a coupon history exists",
            "NOT CYCLE LIFE",
            RED,
        )
        bullets(d, 48, 150, [
            "tau_return,plan is at least the max of tau_el and tau_vent.",
            "On the small-orifice Ecoflex rows, vent dominates. Seconds, not a pure elastic snap.",
            "Twin tau_return_s may sit on that longer planning clock. Stamp: twin is not System ID.",
            "No fatigue count. No duty-cycle rate. No product endurance claim.",
            "C-01 stays OPEN. B-06 stays OPEN. paper only / Critical OPEN.",
        ], 1380, F22)
        footer(d, foot)
        return im

    n = hold(folder, stills, n, 24, title, "vent_title.png")
    frames_anim = 48
    last = None
    for i in range(frames_anim):
        im = timeline(i / (frames_anim - 1))
        save_frame(folder, im, n + i)
        last = im
    if last is not None:
        last.save(MEDIA / "vent_timeline.png")
        stills.append("vent_timeline.png")
    n += frames_anim
    n = hold(folder, stills, n, 36, beats, "vent_beats.png")
    n = hold(folder, stills, n, 36, numbers, "vent_numbers.png")
    n = hold(folder, stills, n, 30, takeaway, "vent_takeaway.png")
    info = encode(folder, n - 1, MEDIA / "vent_vs_elastic_return_review.mp4")
    info["stills"] = stills
    info["label"] = "Vent versus elastic return time-order. Not cycle life."
    report["films"]["B_vent"] = info


def film_c(report):
    folder = RAW / "c_c01"
    fresh(folder)
    stills = []
    n = 1
    foot = [
        "Volumes and masses are ASSUMPTION geometry times TDS density. Not a weighed cast.",
        "Predicted observables are what to record when a coupon exists. Not claimed results.",
        "paper only / Critical OPEN. C-01 stays OPEN. Twin is not System ID. 12 fps authored clock.",
    ]

    def title():
        im, d = new_card(
            "C  ·  C-01 COUPON SIZING",
            "Predicted observables, not a result",
            "C-01 OPEN",
            RED,
        )
        bullets(d, 48, 150, [
            "Source: coupon sizing math, ACCEPTED-A as paper. The Critical stays open.",
            "Wall volume and fill mass use planning (L, r, t) times TDS density.",
            "TB-01 mid is the baseline row: 200 mm, bladder class (30, 4) mm. ASSUMPTION.",
            "Textile clamp lambda_max 1.10 still limits useful axial strain. DESIGN ASSUMPTION.",
            "TB-02-U before F. Shortened coupons stay acceptable as paper. Not product free length.",
        ], 1380, F22)
        footer(d, foot)
        return im

    def mass():
        im, d = new_card(
            "C  ·  VOLUME AND MASS",
            "Baseline row is TB-01 mid",
            "DESIGN ESTIMATE",
            GOLD,
        )
        headers = ["Case  ·  ASSUMPTION", "V wall", "Ecoflex mass", "Lumen"]
        rows = [
            ("TB-01 slim (20/3) x 200 mm", "81.1 cm3", "86.7 g", "—"),
            ("TB-01 mid (30/4) x 200 mm", "160.8 cm3", "172.1 g", "565.5 cm3"),
            ("TB-01 fat (40/5) x 200 mm", "267.0 cm3", "285.7 g", "—"),
            ("TB-02 one chamber x 250 mm", "201.1 cm3", "215.1 g", "706.9 cm3"),
            ("TB-02 x3 mid", "603.2 cm3", "645.4 g", "—"),
        ]
        say(d, (48, 128), "rho Ecoflex 1.07 g/cc TDS. DS20/DS30 1.08 g/cc TDS. Sleeve mass is not in the table.", F16, MUTED)
        xs = [48, 620, 860, 1140]
        y = 170
        for i, htxt in enumerate(headers):
            say(d, (xs[i], y), htxt, F16B, GOLD)
        y = 210
        for idx, row in enumerate(rows):
            fill = (32, 58, 72) if idx == 1 else PANEL
            d.rounded_rectangle((40, y - 8, 1460, y + 64), radius=8, fill=fill, outline=LINE, width=1)
            for i, cell in enumerate(row):
                say(d, (xs[i], y + 8), cell, F18B if idx == 1 else F18, TEXT)
            say(d, (xs[0], y + 36), "DESIGN ESTIMATE arithmetic  ·  not weighed", F15, AMBER)
            y += 84
        say(d, (48, 700), "Highlight is the baseline planning row. Soft free length on the product arm is a different number.", F16, MUTED)
        footer(d, foot)
        return im

    def observables():
        im, d = new_card(
            "C  ·  WHEN A COUPON EXISTS",
            "Record these. Do not claim them yet.",
            "NOT CLAIMED",
            AMBER,
        )
        items = [
            ("TB-01", "P(t), axial delta-L(t), qualitative leak/hold, vent return on one chamber."),
            ("TB-01a", "Same, plus port-boss mount notes. Boss is a geometry class, not a result."),
            ("TB-02-U", "Three branch pressures, tip angle or curvature, coupling. Before F."),
            ("TB-02-F", "Forearm-section bend observables after U learning."),
            ("TB-04", "Tip return history after vent. Compare to the time-order paper. Not cycle life."),
            ("Mass check", "Weigh a dry cast bladder and compare to the fill-mass row."),
        ]
        y = 124
        for name, body in items:
            d.rounded_rectangle((48, y, 1452, y + 92), radius=10, fill=PANEL, outline=LINE, width=2)
            say(d, (68, y + 10), name, F18B, GOLD)
            say(d, (280, y + 12), "predicted observable  ·  not a claimed result", F15B, TEAL)
            for i, wl in enumerate(wrap(d, body, F18, 1320)):
                if i > 1:
                    break
                say(d, (68, y + 42 + i * 22), wl, F18, TEXT)
            y += 100
        footer(d, foot)
        return im

    def sequence():
        im, d = new_card(
            "C  ·  KEYFRAMES",
            "Animation inputs, hero row first",
            "NOT CLAIMED",
            GOLD,
        )
        bullets(d, 48, 132, [
            "K1  Hero (30/4) by 200 mm. ASSUMPTION bench envelope. Not a product free length.",
            "K2  Wall volume 160.8 cm3. DESIGN ESTIMATE.",
            "K3  Ecoflex 172.1 g. Dragon Skin 30 173.7 g. TDS density times volume. Not weighed.",
            "K4  Lumen 0.565 L. ASSUMPTION. It feeds the vent storyboard.",
            "K5  lambda_max 1.10. Fiber clamp about 0.10. DESIGN ASSUMPTION.",
            "K6  Reserve the port boss, Ecoflex primary, TB-01, then TB-02-U before F.",
            "K8  C-01 stays OPEN. Soft stays idle on the live blend. paper only / Critical OPEN.",
        ], 1380, F22, gap=2)
        footer(d, foot)
        return im

    def open_card():
        im, d = new_card(
            "C  ·  STAYS OPEN",
            "Sizing math does not close C-01",
            "CRITICAL OPEN",
            RED,
        )
        bullets(d, 48, 150, [
            "No physical pressure-to-motion evidence is in this film.",
            "Bare strain at ASSUMPTION pressures can exceed the textile clamp. The clamp is about 0.10. DESIGN ASSUMPTION.",
            "Sleeved Ecoflex planning band about 10–80 kPa is a HYPOTHESIS, not a working pressure.",
            "Sensing ranges are not invented on this board.",
            "paper only / Critical OPEN. B-06 stays OPEN. Twin is not System ID.",
        ], 1380, F22)
        footer(d, foot)
        return im

    n = hold(folder, stills, n, 24, title, "c01_size_title.png")
    n = hold(folder, stills, n, 42, mass, "c01_size_mass.png")
    n = hold(folder, stills, n, 36, observables, "c01_size_observables.png")
    n = hold(folder, stills, n, 36, sequence, "c01_size_sequence.png")
    n = hold(folder, stills, n, 30, open_card, "c01_size_open.png")
    info = encode(folder, n - 1, MEDIA / "c01_coupon_sizing_observables_review.mp4")
    info["stills"] = stills
    info["label"] = "Coupon sizing and predicted observables. C-01 stays OPEN."
    report["films"]["C_c01"] = info


def film_d(report):
    folder = RAW / "d_gate"
    fresh(folder)
    stills = []
    n = 1
    foot = [
        "CLOSED-A here means paper or Track A digital. It is not a release.",
        "Twin is not System ID. 12 fps authored review clock.",
        "paper only / Critical OPEN. B-06, C-01, SAF-02, P-05, HY-02 stay OPEN.",
    ]

    def title():
        im, d = new_card(
            "D  ·  STAGE-GATE REFRESH",
            "Digital-done list, matched to the latest papers",
            "NOT A RELEASE",
            GOLD,
        )
        bullets(d, 48, 150, [
            "Feasibility, functional prototype, EV, prod, pilot — still a picture, not a new procedure.",
            "The CLOSED-A digital list now includes the Soft physics and math papers and the Controls digital math papers.",
            "BOM papers sit in that list as paper only.",
            "Critical hardware is unchanged: still OPEN.",
            "Earlier stage-gate film stays in the prior pack. This board is the refresh.",
        ], 1380, F22)
        footer(d, foot)
        return im

    def row():
        im, d = new_card("D  ·  FIVE NAMES", "Where each name sits after the paper accepts", "ILLUSTRATION", GOLD)
        cols = [
            ("1  Feasibility", GREEN, "PAPER", "Track A films plus Soft and Controls ACCEPTED-A papers. Understandable. Not hardware."),
            ("2  Functional prototype", RED, "OPEN", "Coupons and fixtures are not in hand. Critical OPEN."),
            ("3  EV", RED, "OPEN", "Measured identification. The twin is not System ID."),
            ("4  Prod", RED, "OPEN", "Paper BOM is not a released production list. paper only."),
            ("5  Pilot", RED, "OPEN", "Safety evidence and Criticals are not closed."),
        ]
        x = 36
        for title_s, color, state, body in cols:
            d.rounded_rectangle((x, 140, x + 276, 720), radius=12, fill=PANEL, outline=color, width=3)
            for i, wl in enumerate(wrap(d, title_s, F18B, 240)):
                say(d, (x + 16, 160 + i * 26), wl, F18B, TEXT)
            d.rounded_rectangle((x + 16, 230, x + 150, 264), radius=8, fill=color)
            say(d, (x + 28, 236), state, F16B, BG)
            y = 290
            for wl in wrap(d, body, F18, 244):
                say(d, (x + 16, y), wl, F18, MUTED)
                y += 28
            x += 292
        footer(d, foot)
        return im

    def soft():
        im, d = new_card(
            "D  ·  SOFT PAPERS",
            "ACCEPTED-A digital, still not a coupon",
            "PAPER ONLY",
            GREEN,
        )
        bullets(d, 48, 140, [
            "Virtual soft-arm physics. ACCEPTED-A. mu Ecoflex about 39.4 kPa. lambda_max 1.10. Glove 14 oz.",
            "Neo-Hookean pressure to strain to bend. ACCEPTED-A paper. DESIGN ESTIMATE.",
            "Coupon sizing math. ACCEPTED-A paper. Predicted observables only. C-01 stays OPEN.",
            "Vent versus elastic time-order. ACCEPTED-A paper. Not cycle life.",
            "Physics and math integrate, equations E1 through E12. ACCEPTED-A paper.",
            "B-06 keep-out numeric paper is paper only. Critical B-06 stays OPEN.",
            "Soft BOM papers: paper only.",
            "22 Sep teach papers (HUD brief, vent storyboard, coupon animation inputs, digital-done list, ICD dims) are paper only.",
        ], 1380, F22, gap=4)
        footer(d, foot)
        return im

    def controls():
        im, d = new_card(
            "D  ·  CONTROLS PAPERS",
            "ACCEPTED-A digital math, Criticals unchanged",
            "PAPER ONLY",
            GREEN,
        )
        bullets(d, 48, 140, [
            "Presence, inhibit, and session_enable timing. ASSUMPTION. Watchdog what-if is not a new freeze.",
            "Yaw mapping candidates cite the Lead Track A freeze: sign +1, gain 30, clamp 30, idle home_zero, watchdog 2.0 s. Not a measured hardware limit.",
            "C-01 expected-signal note. DESIGN ESTIMATE. C-01 stays OPEN.",
            "Pinch geometry gaps. ASSUMPTION fields. No invented millimeters. No PL. SAF-02 stays OPEN.",
            "Acceptance booleans for the synthetic episodes. Paper only.",
            "Controls BOM papers: paper only. Live-camera ICD is paper. HY-02 the check stays OPEN.",
            "22 Sep Controls papers: pinch blanks, debounce what-if (TBD, not a freeze), stop-topology ASSUMPTION (Lead TBD).",
        ], 1380, F22, gap=4)
        footer(d, foot)
        return im

    def split():
        im, d = new_card("D  ·  SPLIT", "CLOSED-A digital beside Critical OPEN", "DO NOT MIX", GOLD)
        panel(d, (48, 130, 720, 730), "CLOSED-A digital  ·  paper only", [
            "Aim and pedagogy films already on the front door.",
            "RH-02 scoped policy. AF-01b visualization. Pitch pedagogy.",
            "Soft physics, sizing, vent time-order, integrate.",
            "Controls timing, yaw freeze cite, pinch gaps, episode booleans.",
            "BOM papers as paper only.",
            "DESIGN ESTIMATE is not a lab.",
        ], GREEN)
        panel(d, (760, 130, 1452, 730), "Critical OPEN", [
            "B-06 root and pitch structure.",
            "C-01 measured chain. Sizing math does not close it.",
            "SAF-02. Pinch plan does not close it. No PL.",
            "P-05.",
            "HY-02 until an honest face-in-region record or an honest skip.",
            "paper only / Critical OPEN.",
        ], RED)
        footer(d, foot)
        return im

    n = hold(folder, stills, n, 24, title, "gate_refresh_title.png")
    n = hold(folder, stills, n, 30, row, "gate_refresh_five.png")
    n = hold(folder, stills, n, 36, soft, "gate_refresh_soft.png")
    n = hold(folder, stills, n, 36, controls, "gate_refresh_controls.png")
    n = hold(folder, stills, n, 30, split, "gate_refresh_split.png")
    info = encode(folder, n - 1, MEDIA / "stage_gate_digital_done_refresh_review.mp4")
    info["stills"] = stills
    info["label"] = "Stage-gate refresh. CLOSED-A papers are paper only. Criticals stay OPEN."
    report["films"]["D_gate"] = info


def film_e(report):
    folder = RAW / "e_pinch"
    fresh(folder)
    stills = []
    n = 1
    foot = [
        "Every value cell is blank on purpose. ASSUMPTION until measured on a mock.",
        "NO invented mm. NO PL. SAF-02 stays OPEN. P-05 stays OPEN.",
        "paper only / Critical OPEN. Twin stim of a bool is not a geometry measurement. 12 fps authored clock.",
    ]

    gaps_a = [
        ("M-PINCH-01", "Clearance at the pitch hinge. Blank."),
        ("M-PINCH-02", "Clearance at the rotating shoulder band. Blank."),
        ("M-PINCH-03", "Pad thickness at the hinge site. Blank."),
        ("M-PINCH-04", "Pad thickness at the shoulder-band site. Blank."),
        ("M-PINCH-05", "Coverage along the pinch site. Blank."),
        ("M-PINCH-06", "Aperture at a pitch extreme. Blank."),
        ("M-PINCH-07", "Aperture at yaw or carrier extreme. Blank."),
        ("M-PINCH-08", "Travel through the pinch zone, pitch. Blank."),
    ]
    gaps_b = [
        ("M-PINCH-09", "Travel through the pinch zone, yaw or carrier. Blank."),
        ("M-PINCH-10", "Stop reachability. Topology is Lead TBD. Blank."),
        ("M-PINCH-11", "Electronic pinch trip: yes, no, or TBD. Blank."),
        ("M-PINCH-12", "Modality and fail-safe, if a trip is used. Blank."),
        ("M-PINCH-13", "Manual reset after a clear. Blank."),
        ("M-PINCH-14", "Inhibit-stack note. Blank."),
        ("M-PINCH-15", "Person-adjacent evidence list. Blank."),
        ("M-PINCH-16", "Whether a force class is needed. No force number. Blank."),
    ]

    def title():
        im, d = new_card(
            "E  ·  PINCH MEASURE-ON-MOCK",
            "Fields to fill later. Empty now.",
            "SAF-02 OPEN",
            RED,
        )
        bullets(d, 48, 150, [
            "Source: 22 Sep measure-on-mock plan, citing the ACCEPTED-A gaps list. The Critical stays open.",
            "Pinch stays geometry-first. M-PINCH-01 through 16 are blank.",
            "Mushroom mast is an ASSUMPTION pointer. Topology is Lead TBD.",
            "A digital bool stim may exercise inhibit logic. It does not fill these fields.",
            "NO invented mm. NO PL.",
        ], 1380, F22)
        footer(d, foot)
        return im

    def gap_card(kicker, rows):
        im, d = new_card(kicker, "Measure on mock  ·  value not filled", "NO PL", RED)
        say(d, (48, 118), "FIELD", F15B, GOLD)
        say(d, (230, 118), "MEASURAND  ·  ASSUMPTION", F15B, GOLD)
        say(d, (1120, 118), "VALUE", F15B, GOLD)
        y = 146
        for gid, body in rows:
            d.rounded_rectangle((40, y, 1460, y + 66), radius=8, fill=PANEL, outline=LINE, width=2)
            say(d, (56, y + 20), gid, F16B, TEAL)
            say(d, (230, y + 20), body, F16, TEXT)
            d.rounded_rectangle((1100, y + 14, 1440, y + 52), radius=8, fill=(48, 36, 28), outline=AMBER, width=2)
            say(d, (1116, y + 22), "measure on mock", F15B, AMBER)
            y += 72
        footer(d, foot)
        return im

    def keepout():
        im, d = new_card(
            "E  ·  KEEP-OUT CLASSES",
            "Soft ICD classes. Finger gap stays blank.",
            "NOT MEASURED",
            GOLD,
        )
        panel(d, (48, 130, 720, 730), "Pinch classes  ·  no gap filled", [
            "KO_PINCH_PITCH_HINGE",
            "KO_PINCH_PIN_CHEEK",
            "KO_PINCH_BOOT_GUARD",
            "Soft hose stays outside those planes. Class language only.",
            "Finger-gap, pad, aperture, and travel stay on the blank M-PINCH sheet.",
            "Chafe sleeve family stays OPEN until a mock fit-check.",
            "pitch_lock_engaged is the only normative lock bit.",
            "B-06 stays OPEN. SAF-02 stays OPEN.",
        ], RED)
        panel(d, (760, 130, 1452, 730), "Bend floors  ·  DESIGN TARGET", [
            "These are catalog floors, not a measured clearance and not a finger gap.",
            "NITRA 6 mm class: centerline radius at least 12 mm.",
            "NITRA quarter-inch class: at least 12.1 mm.",
            "Festo 6 by 1 minimum: at least 16 mm.",
            "Festo 6 by 1 flow-relevant: prefer at least 26.5 mm.",
            "Eye, boot, and pin-plate structural millimeters stay TBD.",
            "paper only / Critical OPEN. Soft stays idle on the live blend.",
        ], AMBER)
        footer(d, foot)
        return im

    def nonclaim():
        im, d = new_card(
            "E  ·  NON-CLAIM",
            "A blank field is the result of this film",
            "CRITICAL OPEN",
            RED,
        )
        bullets(d, 48, 150, [
            "No clearance, pad, aperture, or travel number is stated.",
            "No force number. No stop-time number. No performance level.",
            "SAF-02 stays Critical OPEN. P-05 stays Critical OPEN.",
            "C-01 and HY-02 are unchanged by this gaps board.",
            "paper only / Critical OPEN.",
        ], 1380, F22)
        footer(d, foot)
        return im

    n = hold(folder, stills, n, 24, title, "pinch_title.png")
    n = hold(folder, stills, n, 36, keepout, "pinch_keepout.png")
    n = hold(folder, stills, n, 42, lambda: gap_card("E  ·  M-PINCH-01 TO 08", gaps_a), "pinch_gaps_a.png")
    n = hold(folder, stills, n, 42, lambda: gap_card("E  ·  M-PINCH-09 TO 16", gaps_b), "pinch_gaps_b.png")
    n = hold(folder, stills, n, 30, nonclaim, "pinch_open.png")
    info = encode(folder, n - 1, MEDIA / "pinch_measure_on_mock_review.mp4")
    info["stills"] = stills
    info["label"] = "Pinch measure-on-mock plan. No invented mm. No PL. SAF-02 stays OPEN."
    report["films"]["E_pinch"] = info


def audit():
    blob = "\n".join(SPOKEN)
    low = blob.lower()
    banned = []
    for word in ("spend", "stephen", "purchase", "dollar", "buy"):
        if word in low:
            banned.append(word)
    if re.search(r"\$", blob):
        banned.append("$")
    if re.search(r"\bpo\b", low):
        banned.append("PO")
    if re.search(r"\bpl\b", low) and "no pl" not in low:
        banned.append("PL-without-refusal")
    # Film E must refuse PL; other films should not invent a PL claim.
    if "no pl" not in low:
        banned.append("missing NO PL")
    required = [
        "39.4",
        "1.10",
        "14 oz",
        "ASSUMPTION",
        "DESIGN ESTIMATE",
        "HYPOTHESIS",
        "not System ID",
        "12 fps",
        "paper only / Critical OPEN",
        "C-01 stays OPEN",
        "SAF-02 stays OPEN",
        "measure on mock",
        "NO invented mm",
    ]
    missing = [r for r in required if r not in blob and r.lower() not in low]
    # case-insensitive check for the phrases already handled; 39.4 is numeric
    missing = [r for r in required if r not in blob]
    if banned or missing:
        raise SystemExit(f"audit failed banned={banned} missing={missing}")


def main():
    MEDIA.mkdir(parents=True, exist_ok=True)
    report = {
        "pass_id": "n3-viz-pack-physics-overlays-board-refresh",
        "fps_note": "12 fps authored review clock. Not a measured camera, detector, or machine rate.",
        "criticals": "B-06, C-01, SAF-02, P-05 stay OPEN. HY-02 stays OPEN. paper only / Critical OPEN.",
        "films": {},
    }
    film_a(report)
    film_b(report)
    film_c(report)
    film_d(report)
    film_e(report)
    audit()
    out = PKT / "media_verification.json"
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: {"frames": v["decoded_frames"], "s": v["duration_s"], "path": v["path"]} for k, v in report["films"].items()}, indent=2))


if __name__ == "__main__":
    main()
