import sys
import img2pdf
import os


def convert_to_pdf(filepath):
    if os.path.isdir(filepath):
        images = [os.path.join(filepath, fname) for fname in os.listdir(filepath) if
               fname.endswith(".jpg") and os.path.isfile(os.path.join(filepath, fname))]
        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert(images))
    elif os.path.isfile(filepath) and filepath.endswith(".jpg"):
        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert(filepath))
    else:
        print("Please input a valid file or directory path.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_or_directory_path>")
    else:
        filepath = sys.argv[1]
        convert_to_pdf(filepath)
