# Builds evidence/img/*: video frame (from scratch/verify cmp top half), rebuild with images, rebuild with img/ blocked (hero + mid-page).
import pathlib, json
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright
SITES = {  # site: (comparison file, frame-half height, scrollY that matches the frame)
 "1-hotel": ("cmp.jpg", 638, 0), "2-festival": ("cmp.jpg", 638, 0), "3-ecommerce": ("cmp_hero.jpg", 634, 0),
 "4-saas": ("cmp2.jpg", 638, 520), "5-drink": ("cmp.jpg", 638, 0), "6-highrise": ("cmp2.jpg", 638, 0), "7-space": ("cmp2.jpg", 638, 0)}
out = pathlib.Path("evidence/img"); meta = {}
def save(pg, path): pg.screenshot(path="evidence/_t.png"); Image.open("evidence/_t.png").convert("RGB").resize((1280, 634)).save(path, quality=82)
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", args=["--use-gl=angle", "--ignore-gpu-blocklist"])
    for s, (cmp, h, y) in SITES.items():
        fr = Image.open(f"scratch/verify/{s[0]}/{cmp}").crop((0, 0, 1280, h)); box = (0, h - 160, 280, h)
        fr.paste(fr.crop(box).filter(ImageFilter.GaussianBlur(30)), box)  # blur the presenter's webcam
        fr.save(out / f"{s}_frame.jpg", quality=82)
        uri = pathlib.Path(f"sites/{s}/index.html").resolve().as_uri(); m = {}
        for mode in ("with", "without"):
            pg = b.new_page(viewport={"width": 1600, "height": 792}, device_scale_factor=0.8)
            blocked = []
            if mode == "without":
                pg.route("**/img/**", lambda r: (blocked.append(r.request.url.split('/img/')[-1]), r.abort()))
            pg.goto(uri); pg.wait_for_timeout(3500)
            pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(1800); save(pg, out / f"{s}_{mode}.jpg")
            if mode == "without":
                H = pg.evaluate("document.documentElement.scrollHeight"); mid = int(H * 0.45)
                pg.evaluate(f"window.scrollTo(0,{mid})"); pg.wait_for_timeout(1800); save(pg, out / f"{s}_without_mid.jpg")
                m.update(height=H, mid=mid, blocked=sorted(set(blocked)))
            pg.close()
        m["files"] = sorted((f.name, round(f.stat().st_size / 1024)) for f in pathlib.Path(f"sites/{s}/img").iterdir())
        m["html_kb"] = round(pathlib.Path(f"sites/{s}/index.html").stat().st_size / 1024); meta[s] = m; print(s, "ok", len(m["blocked"]), "blocked")
    b.close()
pathlib.Path("evidence/_t.png").unlink(); json.dump(meta, open("evidence/meta.json", "w"), indent=1)
