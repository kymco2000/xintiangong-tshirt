from pathlib import Path
import subprocess
import sys
from PIL import Image


PROJECT = Path(__file__).parent
RENDERER = PROJECT / "render_front_logo_equal_height.py"
OUTPUT = PROJECT / "factory_print_files" / "Style1_正面_廟宇印章Logo_朱府千歲宋體古印滿版_10x10cm_300dpi_去背.png"


def test_renderer_creates_transparent_10cm_artwork_with_equal_column_height():
    result = subprocess.run(
        [sys.executable, str(RENDERER)], cwd=PROJECT, capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr

    with Image.open(OUTPUT) as image:
        assert image.size == (1181, 1181)
        assert image.mode == "RGBA"
        assert image.getpixel((0, 0))[3] == 0
        assert tuple(round(value) for value in image.info.get("dpi", ())) == (300, 300)

    # Renderer design contract: enlarged lettering fills the seal while the
    # four-character left column and three-character right column span y=47..274.
    source = RENDERER.read_text(encoding="utf-8")
    assert "RIGHT_FONT_SIZE = 90" in source
    assert "LEFT_FONT_SIZE = 66" in source
    assert "RIGHT_Y = (41, 121, 201)" in source
    assert "LEFT_Y = (41, 101, 161, 221)" in source
    assert "LEFT_X = 100" in source
    assert "RIGHT_X = 220" in source
    assert "LEFT_GLYPH_WIDTH = 120" in source
    assert "RIGHT_GLYPH_WIDTH = 120" in source
    assert "RIGHT_GLYPH_HEIGHT = 78" in source
    assert "LEFT_GLYPH_HEIGHT = 58" in source
    assert 'FONT_PATH = r"C:\\Windows\\Fonts\\NotoSerifTC-VF.ttf"' in source
    assert 'set_variation_by_name("Bold")' in source
    assert "TAIWANESE TEMPLE" not in source


if __name__ == "__main__":
    test_renderer_creates_transparent_10cm_artwork_with_equal_column_height()
    print("PASS: front logo renderer")
