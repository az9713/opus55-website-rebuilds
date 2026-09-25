# Contact sheets: every 2nd frame (1 fps), 5x4 grid, labeled with frame file index.
import os, sys
from PIL import Image, ImageDraw
root = "frames"
for site in sorted(os.listdir(root)):
    d = os.path.join(root, site); files = sorted(f for f in os.listdir(d) if f.startswith("f_"))[::2]
    out = os.path.join("sheets", site); os.makedirs(out, exist_ok=True)
    for s in range(0, len(files), 20):
        sheet = Image.new("RGB", (5*512, 4*288), "black"); dr = ImageDraw.Draw(sheet)
        for i, f in enumerate(files[s:s+20]):
            im = Image.open(os.path.join(d, f)).resize((512, 288))
            x, y = (i % 5)*512, (i//5)*288; sheet.paste(im, (x, y))
            dr.rectangle([x, y, x+90, y+22], fill="yellow"); dr.text((x+4, y+4), f, fill="black")
        sheet.save(os.path.join(out, f"sheet_{s//20:02d}.jpg"), quality=85)
    print(site, len(files))
