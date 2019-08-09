import sys

from src.converter import render_image


if __name__ == "__main__":
    img_argv = sys.argv[1]
    if img_argv == '--img':
        img_path = 'image/' + sys.argv[2]

        render_image(imgpath=img_path)
