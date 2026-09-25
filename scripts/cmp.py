# Usage: python scripts/cmp.py frame.jpg shot.png out.jpg  -> frame (top) over shot (bottom)
import sys
from PIL import Image
f, s, o = sys.argv[1:4]
b = Image.open(f).crop((0, 87, 2545, 1354)).resize((1280, 638)); a = Image.open(s).resize((1280, 638))
c = Image.new("RGB", (1280, 1276)); c.paste(b, (0, 0)); c.paste(a, (0, 638)); c.save(o, quality=85)
