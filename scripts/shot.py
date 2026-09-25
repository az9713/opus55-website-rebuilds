# Usage: python scripts/shot.py sites/1-hotel/index.html out_dir [scrollY ...]
# Screenshots the page in real Chrome at 1600x792 CSS px (same shape as the video viewport), scale 1.6 => 2560 wide.
import sys, os, pathlib
from playwright.sync_api import sync_playwright
page_path, out = sys.argv[1], sys.argv[2]; ys = [int(y) for y in sys.argv[3:]] or [0]
os.makedirs(out, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", args=["--use-gl=angle", "--enable-webgl", "--ignore-gpu-blocklist"])
    pg = b.new_page(viewport={"width": 1600, "height": 792}, device_scale_factor=1.6)
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e))); pg.on("console", lambda m: m.type == "error" and errs.append(m.text))
    pg.goto(pathlib.Path(page_path).resolve().as_uri()); pg.wait_for_timeout(2500)
    for y in ys:
        pg.mouse.wheel(0, 0); pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(1500)
        pg.screenshot(path=os.path.join(out, f"shot_{y:06d}.png"))
    print("page height:", pg.evaluate("document.documentElement.scrollHeight"))
    print("errors:", errs or "none")
    b.close()
