from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
DEMOS = ROOT / "demos"
SOURCE = ROOT.parent / "tmp" / "pdfs" / "annie-render"
FONT = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 36)
BG = (245, 242, 234)


def make_sheet(files, title, output, tile=(480, 270), crop=1.0):
    width, height = tile
    images = []
    for path in files:
        image = Image.open(path).convert("RGB")
        image = image.crop((0, 0, image.width, int(image.height * crop)))
        images.append(ImageOps.fit(image, tile, method=Image.Resampling.LANCZOS))
    cols = 3
    rows = (len(images) + cols - 1) // cols
    canvas = Image.new("RGB", (cols * width, 90 + rows * height + 30), BG)
    ImageDraw.Draw(canvas).text((30, 22), title, font=FONT, fill=(30, 30, 30))
    for index, image in enumerate(images):
        canvas.paste(image, ((index % cols) * width, 90 + (index // cols) * height))
    canvas.save(DEMOS / output, quality=92)


make_sheet(
    [SOURCE / f"page-{n:02}.jpg" for n in [6, 7, 8, 10, 11]],
    "Annie Social Editorial / 推文与运营长图",
    "social-editorial-demo.jpg",
    crop=0.82,
)
make_sheet(
    [DEMOS / name for name in [
        "poster-black-white.png", "poster-cyber.png", "poster-collage.png",
        "poster-ink.png", "poster-orange.png", "poster-vintage.png",
    ]],
    "Annie Poster Design / 六种海报方向",
    "poster-design-demo.jpg",
    tile=(360, 540),
)
make_sheet(
    [SOURCE / f"page-{n:02}.jpg" for n in [16, 17, 18, 19, 20]],
    "Annie Photography Style / 摄影语言",
    "photography-style-demo.jpg",
)
