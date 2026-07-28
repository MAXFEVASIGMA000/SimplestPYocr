import sys
import pytesseract
from PIL import Image

def main():
    if len(sys.argv) < 2:
        print("Usage: python ocr.py image.png")
        return

    image_path = sys.argv[1]

    try:
        img = Image.open(image_path)

        text = pytesseract.image_to_string(
            img,
            config="--psm 6"
        )

        print("\n--- OCR TEXT ---\n")
        print(text)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
