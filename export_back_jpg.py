"""Export the selected Style 1 back artwork as a high-pixel standalone JPG."""

from pathlib import Path

from PIL import Image


PROJECT = Path(__file__).parent
SOURCE = PROJECT / "factory_print_files" / "Style1_背面_平安符朱府千歲_純圖案去背.png"
OUTPUT = PROJECT / "Style1_背面_平安符朱府千歲_獨立圖_4096px_300dpi.jpg"
SIZE = (4096, 5624)


def export() -> Path:
    with Image.open(SOURCE) as source:
        artwork = source.convert("RGB").resize(SIZE, Image.Resampling.LANCZOS)
        artwork.save(OUTPUT, "JPEG", quality=100, subsampling=0, dpi=(300, 300))
    return OUTPUT


if __name__ == "__main__":
    print(export())
