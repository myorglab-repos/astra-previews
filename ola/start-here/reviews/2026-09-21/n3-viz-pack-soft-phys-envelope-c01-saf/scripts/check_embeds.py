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
for v in re.findall(r'<video[^>]+src="([^"]+)"', html):
    p = root / v
    print("VIDEO", v, p.stat().st_size if p.exists() else "ABSENT")
