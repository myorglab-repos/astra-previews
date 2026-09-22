"""Confirm START_HERE still points at real film files, including this pack."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[4]
html = (root / "START_HERE.html").read_text(encoding="utf-8")
srcs = re.findall(r'(?:src|poster)="([^"]+)"', html)
missing = [s for s in srcs if not (root / s).exists()]
print("src_count", len(srcs))
print("missing", len(missing))
for s in missing:
    print("MISSING", s)
required = [
    "reviews/2026-09-22/n3-viz-pack-physics-overlays-board-refresh/media/soft_phys_neohook_overlay_review.mp4",
    "reviews/2026-09-22/n3-viz-pack-physics-overlays-board-refresh/media/vent_vs_elastic_return_review.mp4",
    "reviews/2026-09-22/n3-viz-pack-physics-overlays-board-refresh/media/c01_coupon_sizing_observables_review.mp4",
    "reviews/2026-09-22/n3-viz-pack-physics-overlays-board-refresh/media/stage_gate_digital_done_refresh_review.mp4",
    "reviews/2026-09-22/n3-viz-pack-physics-overlays-board-refresh/media/pinch_measure_on_mock_review.mp4",
    "reviews/2026-09-21/n3-viz-pack-rh02-dfmea-readiness-hy02/media/rh02_partial_extension_staging_review.mp4",
    "reviews/2026-09-21/n3-viz-pack-rh02-dfmea-readiness-hy02/media/b06_option_b_dfmea_storyboard_review.mp4",
    "reviews/2026-09-21/n3-viz-pack-rh02-dfmea-readiness-hy02/media/stage_gate_readiness_review.mp4",
    "reviews/2026-09-21/n3-viz-pack-rh02-dfmea-readiness-hy02/media/stephen_vs_digital_open_items_review.mp4",
    "reviews/2026-09-21/n3-viz-pack-rh02-dfmea-readiness-hy02/media/hy02_office_usb_lr_checklist_review.mp4",
    "reviews/2026-09-21/n3-viz-pack-rh02-dfmea-readiness-hy02/media/live_camera_twin_icd_review.mp4",
    "reviews/2026-09-19/n3-standoff-pitch-policy/media/atlas_review.mp4",
    "reviews/2026-09-19/n3-af01b-exposed-arm-swell-2/media/exposed_blind_review.mp4",
    "reviews/2026-09-19/n3-af01b-exposed-arm-swell-2/media/airflow_review.mp4",
    "reviews/2026-09-21/n3-b06-pitch-height-pedagogy/media/pitch_height_review.mp4",
    "reviews/2026-09-21/n3-viz-pack-soft-phys-envelope-c01-saf/media/head_yaw_review_slim_root.mp4",
    "reviews/2026-09-21/n3-viz-pack-soft-phys-envelope-c01-saf/media/soft_phys_cues_review.mp4",
    "reviews/2026-09-21/n3-head-yaw-live-usb-path/media/head_yaw_review_black_collars.mp4",
    "reviews/2026-09-21/n3-viz-pack-soft-phys-envelope-c01-saf/media/b06_envelope_keepout_review.mp4",
    "reviews/2026-09-21/n3-viz-pack-soft-phys-envelope-c01-saf/media/c01_coupon_geometry_review.mp4",
    "reviews/2026-09-21/n3-viz-pack-soft-phys-envelope-c01-saf/media/saf02_presence_inhibit_hil_review.mp4",
    "reviews/2026-09-19/n3-rh02-partial-extension/media/partial_short.png",
]
for s in required:
    if s not in html:
        print("NOT IN HTML", s)
    elif not (root / s).exists():
        print("ABSENT FILE", s)
    else:
        print("OK", s, (root / s).stat().st_size)
if missing or any(s not in html or not (root / s).exists() for s in required):
    raise SystemExit(1)
