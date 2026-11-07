import os
import shutil
from PIL import Image, ImageDraw

RES = "android/app/src/main/res"
shutil.rmtree(RES + "/mipmap-anydpi-v26", ignore_errors=True)
src = Image.open("icon.png").convert("RGB")
sizes = {
    "mdpi": 48,
    "hdpi": 72,
    "xhdpi": 96,
    "xxhdpi": 144,
    "xxxhdpi": 192,
}
for d in sizes:
    n = sizes[d]
    pasta = RES + "/mipmap-" + d + "/"
    a = src.resize((n, n), Image.Resampling.LANCZOS)
    a.save(pasta + "ic_launcher.png")
    a.save(pasta + "ic_launcher_foreground.png")
    m = Image.new("L", (n, n), 0)
    ImageDraw.Draw(m).ellipse((0, 0, n - 1, n - 1), fill=255)
    r = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    r.paste(a, (0, 0), m)
    r.save(pasta + "ic_launcher_round.png")
print("icones ok")
