"""Teaching boards for the RH-02 / DFMEA / readiness / HY-02 viz pack.

12 fps is the authored review clock. It is not a measured camera, detector,
or machine rate. Cards are illustrations. They do not close Criticals.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[4]
PKT = Path(__file__).resolve().parents[1]
MEDIA = PKT / "media"
RAW = PKT / "raw"
RH_MEDIA = ROOT / "reviews" / "2026-09-19" / "n3-rh02-partial-extension" / "media"

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
WHITE = (249, 245, 239)

FONT = "C:/Windows/Fonts/segoeui.ttf"
BOLD = "C:/Windows/Fonts/segoeuib.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)


F16 = font(16)
F16B = font(16, True)
F18 = font(18)
F18B = font(18, True)
F20B = font(20, True)
F22 = font(22)
F22B = font(22, True)
F28B = font(28, True)
F34B = font(34, True)


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
    d.text((36, 22), kicker, font=F16B, fill=GOLD)
    d.text((36, 48), title, font=F34B, fill=TEXT)
    if badge:
        bw = d.textlength(badge, font=F16B) + 28
        x0 = W - 36 - bw
        d.rounded_rectangle((x0, 22, x0 + bw, 52), radius=8, fill=badge_fill)
        d.text((x0 + 14, 28), badge, font=F16B, fill=BG)
    return im, d


def footer(d, lines):
    d.rectangle((0, 768, W, H), fill=(12, 22, 34))
    d.rectangle((0, 768, W, 772), fill=GOLD)
    y = 784
    for i, line in enumerate(lines[:4]):
        d.text((36, y), line, font=F16B if i == 0 else F16, fill=GOLD if i == 0 else MUTED)
        y += 24


def panel(d, box, title, body_lines, title_fill=GOLD):
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, radius=12, fill=PANEL, outline=LINE, width=2)
    d.text((x0 + 18, y0 + 14), title, font=F20B, fill=title_fill)
    y = y0 + 52
    max_w = (x1 - x0) - 36
    for line in body_lines:
        for wl in wrap(d, line, F18, max_w):
            if y > y1 - 28:
                return
            d.text((x0 + 18, y), wl, font=F18, fill=TEXT)
            y += 26


def bullets(d, x, y, items, width, fnt=F22, fill=TEXT, gap=8):
    for item in items:
        lines = wrap(d, item, fnt, width - 28)
        d.ellipse((x, y + 8, x + 10, y + 18), fill=GOLD)
        for wl in lines:
            d.text((x + 22, y), wl, font=fnt, fill=fill)
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


def film_a(report):
    folder = RAW / "a_rh02"
    fresh(folder)
    stills = []
    n = 1
    foot = [
        "ASSUMPTION HUD. Not measured reach. 12 fps = authored review clock, not a detector rate.",
        "Bar lengths are drawing aids. Prior digital policy audit is not re-run here. Twin is not System ID.",
        "RH-02 scoped policy stays CLOSED-A. This film does not close B-06, C-01, SAF-02, or P-05. No spend.",
    ]

    def title():
        im, d = new_card(
            "A  ·  RH-02 PARTIAL-EXTENSION STAGING",
            "Full stroke vs staged extension",
            "NOT MEASURED REACH",
            AMBER,
        )
        bullets(d, 48, 130, [
            "Teaching picture of the existing RH-02 aim policy. Not a new reach test.",
            "Full extension stays the normal head-punch case.",
            "Half-stroke (50%) is NON-HEAD-TARGET. Amber marks a reference only.",
            "Staged 70% keeps the head-target class from that policy. This film does not re-measure it.",
            "50% head shots stay unavailable until a later mechanical or policy brief.",
        ], 1380, F22)
        footer(d, foot)
        return im

    def stages():
        im, d = new_card(
            "A  ·  DRAWING AID  ·  NOT A CHORD IN MILLIMETERS",
            "Three teaching classes",
            "DRAWING AID",
            AMBER,
        )
        rows = [
            (1180, GREEN, "FULL", "Normal head-punch case. Policy class. Not a measured chord."),
            (820, TEAL, "70% STAGED", "Head-target class retained by the prior policy. Not re-measured here."),
            (590, AMBER, "50% HALF", "NON-HEAD-TARGET. Amber reference only. Not a hit zone."),
        ]
        y = 140
        for width, color, name, note in rows:
            d.rounded_rectangle((48, y, 48 + width, y + 64), radius=10, fill=color)
            d.text((64, y + 16), name, font=F22B, fill=BG)
            d.text((48, y + 76), note, font=F18, fill=MUTED)
            y += 160
        footer(d, foot)
        return im

    def half():
        im, d = new_card(
            "A  ·  HALF-STROKE",
            "50% is not a head shot",
            "NON-HEAD-TARGET",
            AMBER,
        )
        panel(d, (48, 130, 1452, 730), "What the prior policy said", [
            "Six 50% straights were labeled NON-HEAD-TARGET.",
            "Amber boxes are separated diagnostic references, not hit zones.",
            "Motion and mesh were not changed for that policy pass.",
            "Quantified misses in the prior audit stay in that assessment. They are not restated here as a new measurement.",
            "Do not train or caption a 50% straight as a head punch.",
        ], AMBER)
        footer(d, foot)
        return im

    def seventy():
        im, d = new_card(
            "A  ·  STAGED 70%",
            "Head-target class, not a new audit",
            "POLICY CLASS",
            TEAL,
        )
        panel(d, (48, 130, 1452, 730), "Held from the prior digital policy", [
            "Six 70% straights kept the head-target class: surface inclusion and centroid-height language from that audit.",
            "A tall residual was reported in the RH-02 assessment. This film does not re-measure it and does not treat surface inclusion as centered aim.",
            "The word cyan on the old stills is that policy mark. It is not the retired shoulder-pad color.",
            "Not loaded reach. Not contact force. Not cycle life.",
        ], TEAL)
        footer(d, foot)
        return im

    def stills_card():
        im, d = new_card(
            "A  ·  INHERITED STILLS",
            "Short, mid, tall — prior sheets",
            "NOT A RE-AUDIT",
            AMBER,
        )
        names = [
            ("partial_short.png", "short"),
            ("partial_mid.png", "mid"),
            ("partial_tall.png", "tall"),
        ]
        x = 48
        for filename, label in names:
            shot = Image.open(RH_MEDIA / filename).convert("RGB")
            shot.thumbnail((450, 500), Image.Resampling.LANCZOS)
            im.paste(shot, (x, 130))
            d = ImageDraw.Draw(im)
            d.rectangle((x, 130, x + shot.width, 168), fill=(16, 28, 42))
            d.text((x + 10, 136), f"{label}  ·  prior policy still", font=F16B, fill=GOLD)
            x += shot.width + 18
        d = ImageDraw.Draw(im)
        d.text((48, 680), "Inherited from reviews/2026-09-19/n3-rh02-partial-extension/media. Not measured reach.", font=F18, fill=MUTED)
        footer(d, foot)
        return im

    for painter, still, frames in (
        (title, "rh02_title.png", 30),
        (stages, "rh02_stages.png", 36),
        (half, "rh02_half.png", 30),
        (seventy, "rh02_seventy.png", 30),
        (stills_card, "rh02_stills.png", 36),
    ):
        n = hold(folder, stills, n, frames, painter, still)
    count = n - 1
    info = encode(folder, count, MEDIA / "rh02_partial_extension_staging_review.mp4")
    info["stills"] = stills
    info["label"] = "ASSUMPTION teaching of RH-02 policy. Not measured reach. Does not close Criticals."
    report["films"]["A_rh02"] = info


def film_b(report):
    folder = RAW / "b_dfmea"
    fresh(folder)
    stills = []
    n = 1
    foot = [
        "ASSUMPTION storyboard. No RPN. S/O/D stay blank. No invented severity, force, or cycle life.",
        "Normative lock bit is pitch_lock_engaged only. B-06 stays Critical OPEN. No PO. No spend.",
        "12 fps = authored review clock, not a measured detector. Twin is not System ID.",
    ]

    def title():
        im, d = new_card("B  ·  B-06 OPTION B DFMEA", "Failure modes as teaching cards", "CRITICAL OPEN", RED)
        bullets(d, 48, 140, [
            "Soft-side and interface rows only. Starter DFMEA. Not a closed analysis.",
            "Cards in this film: pinch, chafe, lock bit, boot recess.",
            "Severity, occurrence, and detection are blank on purpose.",
            "These rows support B-06. They do not close it.",
        ], 1380, F22)
        footer(d, foot)
        return im

    def pinch():
        im, d = new_card("B  ·  PINCH", "Hinge gap and service pinch", "NO RISK SCORE", RED)
        panel(d, (48, 130, 720, 730), "F-08  pitch hinge", [
            "Failure mode: pinch at the pitch hinge.",
            "Local effect: soft-tissue injury. System effect: safety incident.",
            "Intent: padding, guards, and soft hose outside the pinch planes.",
            "Owner: Safety primary. Soft supports the keep-out story.",
            "Not a measured gap. Not a finger-clearance number.",
        ], RED)
        panel(d, (760, 130, 1452, 730), "F-08a  pin change", [
            "Failure mode: operator pinch while changing the pin, with soft services present.",
            "Cause class: hose routed through the cheek gap.",
            "Intent: service routing clear of the pin path.",
            "Action class: Soft service narrative plus Lead DFA.",
            "Procedure review is intent. Not a completed safety gate.",
        ], AMBER)
        footer(d, foot)
        return im

    def chafe():
        im, d = new_card("B  ·  CHAFE", "Hose pinch, lip wear, flex-loop", "NO CYCLE LIFE", AMBER)
        panel(d, (48, 130, 500, 730), "F-04  pinch / crack", [
            "Hose pinch or fatigue crack at the pitch hinge.",
            "Chamber can go limp or stick.",
            "Intent: flex-loop, catalog bend class, edge radius, hose outside pinch planes.",
            "No invented life.",
        ], AMBER)
        panel(d, (524, 130, 976, 730), "F-04a  chafe", [
            "Chafe at boot lip, textile eye, or pin flag.",
            "Intent: sleeve or tape class.",
            "Part number is not frozen.",
            "Unit price for the sleeve class is NOT IN SOURCE here. No PO.",
        ], AMBER)
        panel(d, (1000, 130, 1452, 730), "F-04b  flex-loop", [
            "Loop volume too small at a preset.",
            "Forced kink at short, mid, or tall.",
            "Intent: discrete preset keep-outs. Do not lengthen the continuum to buy loop.",
            "Fit-check waits on a mock. Not done.",
        ], AMBER)
        footer(d, foot)
        return im

    def lockbit():
        im, d = new_card("B  ·  LOCK BIT", "pitch_lock_engaged is the only lock bit", "NOT S3", RED)
        panel(d, (48, 130, 1452, 730), "F-01  pitch unlock / free-fall class", [
            "Function: hold pitch under gravity and punch reaction.",
            "Failure mode: pin not engaged, or flag not home. Arm can drop.",
            "Intent: detent or ball-lock, visual flag, hard stops. Detection intent is a limit or plunger into pitch_lock_engaged.",
            "Soft must not imply physical arms (S3) without that bit.",
            "Mech owns the cam and flag. This card does not close the mechanism.",
            "No invented torque. No invented severity number.",
        ], RED)
        footer(d, foot)
        return im

    def boot():
        im, d = new_card("B  ·  BOOT RECESS", "Textile eye, stitch, bladder neck", "NOT A PEEL TEST", AMBER)
        panel(d, (48, 130, 500, 730), "F-03  eye peel", [
            "Textile eye peel or pull-out.",
            "Soft arm can detach at the root.",
            "Intent: recessed boot, strain relief, harness as the primary load path.",
            "Not a measured peel load.",
        ], AMBER)
        panel(d, (524, 130, 976, 730), "F-03a  stitch", [
            "Stitch unravel or harness fray.",
            "Progressive loosen, then the same detach risk.",
            "Intent: stitch-class schedule and an inspectable edge.",
            "Inspection interval is TBD. No life number.",
        ], AMBER)
        panel(d, (1000, 130, 1452, 730), "F-03b  neck", [
            "Tensile load into the bladder neck instead of the harness.",
            "Neck peel or a leak path.",
            "Intent: harness primary. Coupon and neck inspection later.",
            "Not a coupon result.",
        ], AMBER)
        footer(d, foot)
        return im

    def open_card():
        im, d = new_card("B  ·  DOES NOT CLOSE", "B-06 stays Critical OPEN", "CRITICAL OPEN", RED)
        cards = [
            (48, "PINCH", "F-08 / F-08a"),
            (400, "CHAFE", "F-04 / F-04a / F-04b"),
            (752, "LOCK BIT", "pitch_lock_engaged"),
            (1104, "BOOT RECESS", "F-03 / F-03a / F-03b"),
        ]
        for x, name, sub in cards:
            d.rounded_rectangle((x, 150, x + 330, 340), radius=12, fill=PANEL, outline=RED, width=2)
            d.text((x + 18, 180), name, font=F22B, fill=RED)
            for i, wl in enumerate(wrap(d, sub, F18, 290)):
                d.text((x + 18, 230 + i * 28), wl, font=F18, fill=TEXT)
        bullets(d, 48, 380, [
            "Rows not re-owned here: bearing walk-out, encoder, bumper energy, service cartridge, corrosion, over-pressure.",
            "Blank S/O/D until a Lead analysis path. No fake RPN.",
            "Catalog pointers in the source paper are scouts. This film is not a purchase.",
        ], 1380, F22)
        footer(d, foot)
        return im

    for painter, still, frames in (
        (title, "dfmea_title.png", 24),
        (pinch, "dfmea_pinch.png", 30),
        (chafe, "dfmea_chafe.png", 30),
        (lockbit, "dfmea_lock.png", 30),
        (boot, "dfmea_boot.png", 30),
        (open_card, "dfmea_open.png", 30),
    ):
        n = hold(folder, stills, n, frames, painter, still)
    info = encode(folder, n - 1, MEDIA / "b06_option_b_dfmea_storyboard_review.mp4")
    info["stills"] = stills
    info["label"] = "DFMEA teaching cards. No RPN. B-06 stays Critical OPEN."
    report["films"]["B_dfmea"] = info


def film_c(report):
    folder = RAW / "c_gate"
    fresh(folder)
    stills = []
    n = 1
    foot = [
        "ILLUSTRATION of the readiness posture. Not a new stage-gate procedure. Not a release.",
        "CLOSED-A means digital / paper / Track A only. Critical hardware stays OPEN. No PO. No spend.",
        "12 fps = authored review clock. Twin is not System ID. No invented force, FPS, or cycle life.",
    ]

    def title():
        im, d = new_card("C  ·  STAGE-GATE BOARD", "Feasibility through pilot, as a picture", "NOT A RELEASE", GOLD)
        bullets(d, 48, 140, [
            "Five names from the teaching ask: Feasibility, Functional prototype, EV, Prod, Pilot.",
            "This board maps those names onto work already labeled CLOSED-A digital or Critical OPEN.",
            "It does not create a manufacturing gate and it does not close one.",
            "Films, papers, and the twin do not authorize a buy.",
        ], 1380, F22)
        footer(d, foot)
        return im

    def row():
        im, d = new_card("C  ·  FIVE NAMES", "Where each name sits today", "ILLUSTRATION", GOLD)
        cols = [
            ("1  Feasibility", GREEN, "DIGITAL", "Track A films, aim policy, paper ICDs. Understandable. Not hardware."),
            ("2  Functional prototype", RED, "OPEN", "Mock boot, coupons, fixtures. Needs Stephen when authorized. Not started here."),
            ("3  EV", RED, "OPEN", "Measured identification. The twin is not System ID."),
            ("4  Prod", RED, "OPEN", "No production BOM release. No PO from this pack."),
            ("5  Pilot", RED, "OPEN", "Safety, Criticals, and field evidence are not in hand."),
        ]
        x = 36
        for title_s, color, state, body in cols:
            d.rounded_rectangle((x, 140, x + 276, 720), radius=12, fill=PANEL, outline=color, width=3)
            for i, wl in enumerate(wrap(d, title_s, F18B, 240)):
                d.text((x + 16, 160 + i * 26), wl, font=F18B, fill=TEXT)
            d.rounded_rectangle((x + 16, 230, x + 160, 264), radius=8, fill=color)
            d.text((x + 28, 236), state, font=F16B, fill=BG)
            y = 290
            for wl in wrap(d, body, F18, 240):
                d.text((x + 16, y), wl, font=F18, fill=MUTED)
                y += 28
            x += 292
        footer(d, foot)
        return im

    def feasibility():
        im, d = new_card("C  ·  FEASIBILITY", "Digital CLOSED-A is not a prototype", "CLOSED-A DIGITAL", GREEN)
        bullets(d, 48, 140, [
            "Track A reach, pitch, airflow, and RH-02 policy films and stills are reviewable.",
            "RH-02 partial-extension policy is CLOSED-A for that scoped digital aim rule. 50% head shots stay unavailable.",
            "Soft virtual physics is a DESIGN ESTIMATE paper. It is not System ID.",
            "Live-camera ICD and the HY-02 checklist are paper. HY-02 the check stays OPEN.",
            "Yaw gain, clamp, and watchdog in the ICD are Lead Track A freeze values, not measured hardware limits.",
        ], 1380, F22)
        footer(d, foot)
        return im

    def hardware():
        im, d = new_card("C  ·  PROTOTYPE AND EV", "Hardware evidence is still missing", "CRITICAL OPEN", RED)
        panel(d, (48, 130, 720, 730), "Functional prototype — OPEN", [
            "B-06 root structure is not a prototype.",
            "ABS mock boot and Mech fixture samples are spend, not this film.",
            "C-01 coupons are not cast.",
            "No purchase order.",
        ], RED)
        panel(d, (760, 130, 1452, 730), "EV — OPEN", [
            "Engineering validation needs measured pressure, motion, and contact.",
            "Digital Track B prep is a plan. It does not close C-01.",
            "Presence on the USB path may be a simulated bool. That is not a gym sensor.",
            "Twin overlays are not a durability test.",
        ], RED)
        footer(d, foot)
        return im

    def prod():
        im, d = new_card("C  ·  PROD AND PILOT", "Neither gate is open for release", "NO PO", RED)
        panel(d, (48, 130, 720, 730), "Prod — OPEN", [
            "Build-intent BOM is a paper scout. It is not a released production BOM.",
            "Supplier examples in source papers are not orders.",
            "DFM, CAD millimeters, and a pilot kit are not frozen here.",
            "No spend.",
        ], RED)
        panel(d, (760, 130, 1452, 730), "Pilot — OPEN", [
            "Pilot wants Critical safety, C-01, B-06, and controls closed with evidence.",
            "SAF-02 and P-05 stay OPEN.",
            "HY-02 gym or office face-in-ROI evidence is not in this pack.",
            "This illustration is not a field unit.",
        ], RED)
        footer(d, foot)
        return im

    def split():
        im, d = new_card("C  ·  SPLIT", "CLOSED-A digital beside Critical OPEN", "DO NOT MIX", GOLD)
        panel(d, (48, 130, 720, 730), "CLOSED-A digital", [
            "Aim and pedagogy films, including this teaching pack once reviewed.",
            "RH-02 scoped policy. AF-01b visualization. Pitch pedagogy.",
            "Paper ICD, DFMEA starter, coupon geometry, checklist.",
            "DESIGN ESTIMATE soft physics. Not a lab.",
        ], GREEN)
        panel(d, (760, 130, 1452, 730), "Critical OPEN hardware", [
            "B-06 root / pitch structure.",
            "C-01 measured impact chain.",
            "SAF-02 and P-05.",
            "HY-02 stays OPEN until an honest face-in-ROI record or an honest skip is accepted. This film does not supply L/R.",
        ], RED)
        footer(d, foot)
        return im

    for painter, still, frames in (
        (title, "gate_title.png", 24),
        (row, "gate_five.png", 36),
        (feasibility, "gate_feasibility.png", 30),
        (hardware, "gate_prototype_ev.png", 30),
        (prod, "gate_prod_pilot.png", 30),
        (split, "gate_split.png", 30),
    ):
        n = hold(folder, stills, n, frames, painter, still)
    info = encode(folder, n - 1, MEDIA / "stage_gate_readiness_review.mp4")
    info["stills"] = stills
    info["label"] = "Readiness illustration. CLOSED-A digital vs Critical OPEN. Not a release."
    report["films"]["C_stage_gate"] = info


def film_d(report):
    folder = RAW / "d_stephen"
    fresh(folder)
    stills = []
    n = 1
    foot = [
        "ASSUMPTION split from the Soft open-items brief. Digital close is paper only.",
        "No PO. Spend order across Soft and Mech is Lead / Michael OPEN. Soft does not open the buy.",
        "C-01 OPEN. B-06 OPEN. 12 fps authored review clock. No invented force, FPS, or cycle life.",
    ]

    def title():
        im, d = new_card("D  ·  STEPHEN VS DIGITAL", "Two columns. No purchase.", "NO PO", GOLD)
        bullets(d, 48, 150, [
            "Left: what the digital and paper passes already did at $0.",
            "Right: what still needs Stephen when someone authorizes spend.",
            "Neither column closes a Critical.",
            "This film does not choose which band goes first.",
        ], 1380, F22)
        footer(d, foot)
        return im

    def both():
        im, d = new_card("D  ·  THE BOARD", "Done digitally  ·  still needs Stephen", "NO PO", GOLD)
        panel(d, (48, 130, 720, 730), "Digital done  ·  $0", [
            "Soft twin hooks as DESIGN ESTIMATE proposals. Not System ID. Not a live blend freeze.",
            "C-01 geometry and coupon sequence on paper. Not a cast kit.",
            "B-06 keep-outs, mock path, and DFMEA rows on paper. Not fab. Not CAD millimeters.",
            "This Stephen-versus-digital map.",
        ], GREEN)
        panel(d, (760, 130, 1452, 730), "Needs Stephen  ·  no PO", [
            "Soft TB-01 and TB-02 cast kit. TB-02-U before F. Separate from Mech.",
            "TB-03 wrist and TB-04 return consumables later, unless Lead reorders.",
            "Mech ABS mock boot, then pin / plate / bushing / bumper / fastener / tube samples.",
            "Textile-eye peel coupons later. Chafe sleeve part number after the mock. Elias picks sensing SKUs, not Soft.",
        ], AMBER)
        footer(d, foot)
        return im

    def wait():
        im, d = new_card("D  ·  STILL WAITING", "Paper does not spend", "LEAD OPEN", AMBER)
        bullets(d, 48, 140, [
            "Lead disposition on the deepen set can land without a buy.",
            "Live Blender soft-body remake is a non-gate until Lead asks.",
            "Numeric Soft ICD dimensions wait on Lead CAD.",
            "Chafe sleeve family stays unfrozen until an ABS mock fit-check.",
            "Who goes first — Soft cast kit or Mech mock — stays an open question. This film does not answer it.",
        ], 1380, F22)
        footer(d, foot)
        return im

    def criticals():
        im, d = new_card("D  ·  CRITICALS", "Digital done is not hardware done", "STILL OPEN", RED)
        panel(d, (48, 130, 720, 730), "C-01  OPEN", [
            "Specimen geometry is paper.",
            "Measured pressure to motion to contact is still required.",
            "Track B then Track C. No person in the Soft Track B contact story.",
        ], RED)
        panel(d, (760, 130, 1452, 730), "B-06  OPEN", [
            "Soft ICD, keep-outs, mock path, and DFMEA rows support the Critical.",
            "Structural CAD, FEA, and a prototype stay with Lead.",
            "This column split does not close it.",
        ], RED)
        footer(d, foot)
        return im

    for painter, still, frames in (
        (title, "stephen_title.png", 24),
        (both, "stephen_board.png", 42),
        (wait, "stephen_wait.png", 30),
        (criticals, "stephen_criticals.png", 30),
    ):
        n = hold(folder, stills, n, frames, painter, still)
    info = encode(folder, n - 1, MEDIA / "stephen_vs_digital_open_items_review.mp4")
    info["stills"] = stills
    info["label"] = "Stephen vs digital board. No PO. C-01 and B-06 stay OPEN."
    report["films"]["D_stephen"] = info


def film_e(report):
    folder = RAW / "e_hy02"
    fresh(folder)
    stills = []
    n = 1
    foot = [
        "HY-02 stays OPEN. Honest SKIPPED until a face is in the ROI. This film invents no L/R result.",
        "Checklist is paper. DIGITAL_TWIN_ONLY. No webcam media by default. No physical yaw or strike.",
        "12 fps = authored review clock, not a detector rate. No accuracy, IoU, or latency bar.",
    ]

    def title():
        im, d = new_card("E  ·  HY-02 OFFICE USB", "Operator checklist. Not a result.", "HY-02 OPEN", RED)
        bullets(d, 48, 140, [
            "Office USB is allowed for a first qualitative L/R spot-check. A product camera is not required for that first check.",
            "The check has not been recorded with a single face in the region of interest.",
            "Current gym spot-check file: SKIPPED_NO_OPERATOR_APPROVAL. Stills empty. Film null.",
            "Do not read this teaching film as left/right evidence.",
        ], 1380, F22)
        footer(d, foot)
        return im

    def steps_a():
        im, d = new_card("E  ·  STEPS 1–4", "Before any claim", "NO L/R YET", AMBER)
        steps = [
            "1  Plug the office USB webcam. Confirm the operating system sees a device.",
            "2  One face alone in the ROI. Empty or several faces: record that token. Do not invent a side.",
            "3  Change to reviews/n3-head-track-yaw-bridge/ (or the desk mirror of that script).",
            "4  Flags: --camera INDEX is an ASSUMPTION. Add --head-spotcheck-approved and --sim-present. Preview and JSONL log are optional.",
        ]
        bullets(d, 48, 140, steps, 1380, F22)
        footer(d, foot)
        return im

    def steps_b():
        im, d = new_card("E  ·  STEPS 5–7", "Honest record, then stop", "NO L/R YET", AMBER)
        steps = [
            "5  Run only when a face is actually in frame. Preview text, if used, is SIM presence and DIGITAL TWIN ONLY.",
            "6  Write the honest JSON outcome only. Stdout, opt-in JSONL, or an operator note. No invented stills.",
            "7  Stop. Do not mark HY-02 closed. Hand the evidence path to Ola.",
            "If there is no camera: record SKIPPED_NO_CAMERA. That skip is not a failure. Software may continue on a clip.",
        ]
        bullets(d, 48, 140, steps, 1380, F22)
        footer(d, foot)
        return im

    def skipped():
        im, d = new_card("E  ·  ON DISK TODAY", "SKIPPED until face-in-ROI", "SKIPPED", RED)
        d.rounded_rectangle((48, 140, 1452, 520), radius=16, fill=(48, 24, 28), outline=RED, width=3)
        d.text((80, 170), "SKIPPED_NO_OPERATOR_APPROVAL", font=F34B, fill=RED)
        lines = [
            "Source: reviews/2026-09-21/n3-head-yaw-live-usb-path/gym_spotcheck.json",
            "stills: []      film: null",
            "Note on that file: camera may be present, but the operator flags were not both set.",
            "No left result. No right result. No still. No spot-check film.",
        ]
        y = 250
        for line in lines:
            d.text((80, y), line, font=F22, fill=TEXT)
            y += 44
        d.text((48, 560), "Presence flag in the example command is simulated. It is not a time-of-flight sensor.", font=F18, fill=MUTED)
        d.text((48, 600), "Camera index in the example is an ASSUMPTION. Confirm the OpenCV index on the machine.", font=F18, fill=MUTED)
        footer(d, foot)
        return im

    def tokens():
        im, d = new_card("E  ·  TOKENS", "Names only. No pass invented.", "NO PASS_LR", RED)
        rows = [
            ("SKIPPED_NO_CAMERA", "Skip, not a fail. No device."),
            ("SKIPPED_NO_OPERATOR_APPROVAL", "Current file. No L/R media."),
            ("CAMERA_OPEN_FAILED", "Open was attempted and failed."),
            ("CAMERA_PRESENT_NO_SINGLE_FACE", "Open, but not exactly one face."),
            ("CAMERA_PRESENT_MULTI_FACE", "Several faces. Head invalid."),
            ("HEAD_SPOTCHECK_APPROVED_ONE_FACE", "Qualitative gate only. Does not close HY-02 by itself."),
        ]
        y = 130
        for name, meaning in rows:
            d.rounded_rectangle((48, y, 760, y + 78), radius=8, fill=PANEL, outline=LINE, width=2)
            d.text((64, y + 12), name, font=F16B, fill=GOLD)
            d.text((64, y + 40), meaning, font=F16, fill=TEXT)
            y += 92
        d.rounded_rectangle((800, 130, 1452, 682), radius=12, fill=(48, 24, 28), outline=RED, width=3)
        d.text((824, 160), "Not in this film", font=F28B, fill=RED)
        for i, line in enumerate([
            "No PASS_LR token.",
            "No left still.",
            "No right still.",
            "No accuracy number.",
            "No detector rate.",
            "Code may not emit every token yet. The names are checklist language.",
        ]):
            d.text((824, 230 + i * 64), line, font=F22, fill=TEXT)
        footer(d, foot)
        return im

    for painter, still, frames in (
        (title, "hy02_title.png", 30),
        (steps_a, "hy02_steps_1.png", 30),
        (steps_b, "hy02_steps_2.png", 30),
        (skipped, "hy02_skipped.png", 36),
        (tokens, "hy02_tokens.png", 30),
    ):
        n = hold(folder, stills, n, frames, painter, still)
    info = encode(folder, n - 1, MEDIA / "hy02_office_usb_lr_checklist_review.mp4")
    info["stills"] = stills
    info["label"] = "HY-02 checklist film. SKIPPED_NO_OPERATOR_APPROVAL. No invented L/R."
    report["films"]["E_hy02"] = info


def film_f(report):
    folder = RAW / "f_icd"
    fresh(folder)
    stills = []
    n = 1
    foot = [
        "ASSUMPTION interface picture. Not an accuracy claim. performance_claim stays NONE.",
        "DIGITAL_TWIN_ONLY. Session enable does not authorize a strike. Twin is not System ID.",
        "Gain, clamp, and watchdog are Lead Track A freeze values, not measured hardware limits. 12 fps is the film clock.",
    ]

    def title():
        im, d = new_card("F  ·  LIVE CAMERA / TWIN ICD", "A picture of the interface", "NOT ACCURACY", GOLD)
        bullets(d, 48, 140, [
            "Camera watches a head / human region. Presence is the on-switch for a session.",
            "Office USB may feed the digital twin. It does not drive valves.",
            "Detector class on the USB path is an OpenCV Haar ASSUMPTION. Not an accuracy claim.",
            "One face plus an operator spot-check is the qualitative rule. Confidence cutoff is TBD.",
        ], 1380, F22)
        footer(d, foot)
        return im

    def flow():
        im, d = new_card("F  ·  SIGNAL PATH", "USB or clip, then the twin. Not the arm.", "S0 / S1", TEAL)
        boxes = [
            (48, "USB or clip", "OpenCV index or a file. Index is ASSUMPTION."),
            (400, "capture_head", "schema head-yaw-v1. Scope DIGITAL_TWIN_ONLY."),
            (752, "derive()", "session_enable, yaw_cmd, yaw enable."),
            (1104, "Twin adapter", "Overlay and log. S0/S1. No arm motion."),
        ]
        for x, name, body in boxes:
            d.rounded_rectangle((x, 200, x + 320, 460), radius=12, fill=PANEL, outline=TEAL, width=2)
            d.text((x + 16, 230), name, font=F22B, fill=TEAL)
            y = 290
            for wl in wrap(d, body, F18, 280):
                d.text((x + 16, y), wl, font=F18, fill=TEXT)
                y += 28
        d.text((48, 520), "Not on this path: valves, fill, pressurized strike, physical yaw rotor.", font=F22B, fill=RED)
        d.text((48, 570), "Missing USB is SKIPPED_NO_CAMERA. Clip and HIL may continue. Do not invent a camera.", font=F18, fill=MUTED)
        d.text((48, 620), "Recording stays off unless someone opts into a JSON log. No webcam media by default.", font=F18, fill=MUTED)
        footer(d, foot)
        return im

    def enable():
        im, d = new_card("F  ·  SESSION ENABLE", "Three terms. All must hold.", "NOT S3", GOLD)
        d.rounded_rectangle((48, 150, 1452, 280), radius=12, fill=PANEL, outline=GOLD, width=2)
        d.text((70, 185), "session_enable  =  user_present  AND  head_hypothesis_valid  AND  NOT inhibit_latched", font=F22B, fill=GOLD)
        panel(d, (48, 320, 500, 730), "user_present", [
            "Authoritative for someone at the bag.",
            "On the USB path today: SIMULATED_BOOL_NOT_HARDWARE.",
            "Fault forces absent.",
            "Presence forever blocks physical motion and strike.",
        ], TEAL)
        panel(d, (524, 320, 976, 730), "head hypothesis", [
            "ASSUMPTION: exactly one face.",
            "Plus operator spot-check approval.",
            "Otherwise the head is invalid.",
            "Not an Olympic accuracy bar.",
        ], TEAL)
        panel(d, (1000, 320, 1452, 730), "inhibit", [
            "Latched inhibit kills the session.",
            "Simulated e-stop kills yaw enable.",
            "Manual reset does not start motion.",
            "AI does not clear the latch.",
        ], RED)
        footer(d, foot)
        return im

    def freeze():
        im, d = new_card("F  ·  LEAD FREEZE", "Named values. Not hardware bars.", "NOT MEASURED", AMBER)
        rows = [
            ("normalization", "frame_fraction_0_to_1", "Lead Track A freeze"),
            ("sign", "+1", "NORMATIVE. Positive image x to +Z yaw from home."),
            ("gain_deg_per_signed_x", "30.0", "NOT a measured hardware limit."),
            ("clamp_deg", "30.0", "NOT a measured hardware limit."),
            ("idle_policy", "home_zero", "Accepted digital idle."),
            ("watchdog_s", "2.0", "NOT a measured latency bar."),
        ]
        y = 130
        for name, value, note in rows:
            d.rounded_rectangle((48, y, 1452, y + 88), radius=8, fill=PANEL, outline=LINE, width=2)
            d.text((68, y + 14), name, font=F18B, fill=GOLD)
            d.text((420, y + 14), value, font=F18B, fill=TEXT)
            d.text((68, y + 48), note, font=F16, fill=MUTED)
            y += 100
        footer(d, foot)
        return im

    def stages():
        im, d = new_card("F  ·  STAGES", "S3 is not authorized", "S3 CLOSED", RED)
        cols = [
            ("S0", GREEN, "Record head region and presence flags. Clip or USB. Digital."),
            ("S1", GREEN, "Live lamp, head marker, digital yaw on the twin. No arm motion."),
            ("S2", AMBER, "Simulated continuum from simple cues. Not frozen by this picture."),
            ("S3", RED, "Physical arms. Not authorized. Needs presence interlock, C-01, B-06, and safety."),
        ]
        x = 48
        for name, color, body in cols:
            d.rounded_rectangle((x, 160, x + 340, 640), radius=12, fill=PANEL, outline=color, width=3)
            d.text((x + 20, 190), name, font=F34B, fill=color)
            y = 270
            for wl in wrap(d, body, F20B, 300):
                d.text((x + 20, y), wl, font=F20B, fill=TEXT)
                y += 36
            x += 360
        footer(d, foot)
        return im

    for painter, still, frames in (
        (title, "icd_title.png", 24),
        (flow, "icd_flow.png", 30),
        (enable, "icd_session.png", 30),
        (freeze, "icd_freeze.png", 36),
        (stages, "icd_stages.png", 30),
    ):
        n = hold(folder, stills, n, frames, painter, still)
    info = encode(folder, n - 1, MEDIA / "live_camera_twin_icd_review.mp4")
    info["stills"] = stills
    info["label"] = "ICD illustration. ASSUMPTION. Not accuracy. Not System ID. S3 not authorized."
    report["films"]["F_icd"] = info


def main():
    MEDIA.mkdir(parents=True, exist_ok=True)
    report = {
        "pass_id": "n3-viz-pack-rh02-dfmea-readiness-hy02",
        "fps_note": "12 fps authored review clock. Not a measured camera, detector, or machine rate.",
        "criticals": "B-06, C-01, SAF-02, P-05 stay OPEN. HY-02 stays OPEN. No spend. No PO.",
        "films": {},
    }
    film_a(report)
    film_b(report)
    film_c(report)
    film_d(report)
    film_e(report)
    film_f(report)
    (PKT / "media_verification.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
