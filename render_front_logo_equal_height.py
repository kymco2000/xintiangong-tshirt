"""Render the approved Style 1 front stamp as 10 cm, 300 DPI transparent artwork."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PROJECT = Path(__file__).parent
OUTPUT = (
    PROJECT
    / "factory_print_files"
    / "Style1_正面_廟宇印章Logo_朱府千歲宋體古印滿版_10x10cm_300dpi_去背.png"
)

BASE_CANVAS = 320
CANVAS = 1181  # 10 cm at 300 DPI
SCALE = CANVAS / BASE_CANVAS
STAMP_RED = (154, 43, 43, 255)

# Enlarged type fills the unchanged original stamp border.  Both columns span
# the same visual height (y=47..274 in the base 320 px composition).
RIGHT_FONT_SIZE = 90
LEFT_FONT_SIZE = 66
RIGHT_Y = (41, 121, 201)
LEFT_Y = (41, 101, 161, 221)
LEFT_X = 100
RIGHT_X = 220
LEFT_GLYPH_WIDTH = 120
RIGHT_GLYPH_WIDTH = 120
RIGHT_GLYPH_HEIGHT = 78
LEFT_GLYPH_HEIGHT = 58
FONT_PATH = r"C:\Windows\Fonts\NotoSerifTC-VF.ttf"


def scaled(value: float) -> int:
    return round(value * SCALE)


def centered_text(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, font: ImageFont.FreeTypeFont) -> None:
    bbox = font.getbbox(text)
    width = bbox[2] - bbox[0]
    # Retains the centering convention of the approved original stamp artwork.
    draw.text((x - width // 2, y), text, font=font, fill=STAMP_RED)


def traditional_serif_font(size: int) -> ImageFont.FreeTypeFont:
    font = ImageFont.truetype(FONT_PATH, scaled(size))
    font.set_variation_by_name("Bold")
    return font


def stretched_centered_text(
    image: Image.Image, x: int, top: int, text: str, font: ImageFont.FreeTypeFont, width: int, height: int
) -> None:
    """Place each glyph in an equal, tightly packed traditional seal cell."""
    bbox = font.getbbox(text)
    glyph_width = bbox[2] - bbox[0]
    glyph_height = bbox[3] - bbox[1]
    glyph = Image.new("RGBA", (glyph_width, glyph_height), (255, 255, 255, 0))
    ImageDraw.Draw(glyph).text((-bbox[0], -bbox[1]), text, font=font, fill=STAMP_RED)
    glyph = glyph.resize((width, height), Image.Resampling.LANCZOS)
    image.alpha_composite(glyph, (x - width // 2, top))


def render() -> Path:
    image = Image.new("RGBA", (CANVAS, CANVAS), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    margin = scaled(25)
    draw.rounded_rectangle(
        [margin, margin, CANVAS - margin, CANVAS - margin],
        radius=scaled(24), outline=STAMP_RED, width=scaled(10)
    )
    draw.rounded_rectangle(
        [scaled(39), scaled(39), CANVAS - scaled(39), CANVAS - scaled(39)],
        radius=scaled(16), outline=STAMP_RED, width=scaled(3)
    )

    right_font = traditional_serif_font(RIGHT_FONT_SIZE)
    left_font = traditional_serif_font(LEFT_FONT_SIZE)
    for char, y in zip("信天宮", RIGHT_Y):
        stretched_centered_text(
            image, scaled(RIGHT_X), scaled(y), char, right_font, scaled(RIGHT_GLYPH_WIDTH)
            , scaled(RIGHT_GLYPH_HEIGHT)
        )
    for char, y in zip("朱府千歲", LEFT_Y):
        stretched_centered_text(
            image, scaled(LEFT_X), scaled(y), char, left_font, scaled(LEFT_GLYPH_WIDTH)
            , scaled(LEFT_GLYPH_HEIGHT)
        )

    draw.arc(
        [CANVAS - scaled(65), scaled(20), CANVAS - scaled(20), scaled(65)],
        start=180, end=360, fill=STAMP_RED, width=scaled(4)
    )
    draw.arc(
        [scaled(20), CANVAS - scaled(65), scaled(65), CANVAS - scaled(20)],
        start=0, end=180, fill=STAMP_RED, width=scaled(4)
    )

    image.save(OUTPUT, "PNG", dpi=(300, 300))
    return OUTPUT


if __name__ == "__main__":
    print(render())
