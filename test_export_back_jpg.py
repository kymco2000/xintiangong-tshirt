from pathlib import Path
import subprocess
import sys

from PIL import Image


PROJECT = Path(__file__).parent
EXPORTER = PROJECT / "export_back_jpg.py"
OUTPUT = PROJECT / "Style1_背面_平安符朱府千歲_獨立圖_4096px_300dpi.jpg"


def test_exporter_creates_high_resolution_standalone_jpg():
    result = subprocess.run(
        [sys.executable, str(EXPORTER)], cwd=PROJECT, capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr
    with Image.open(OUTPUT) as image:
        assert image.format == "JPEG"
        assert image.mode == "RGB"
        assert image.size == (4096, 5624)
        assert tuple(round(value) for value in image.info.get("dpi", ())) == (300, 300)


if __name__ == "__main__":
    test_exporter_creates_high_resolution_standalone_jpg()
    print("PASS: high-resolution standalone back JPG")
