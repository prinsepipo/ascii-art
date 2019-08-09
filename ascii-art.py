import sys

from src.converter import render_image


if __name__ == "__main__":
    img_path = 'image/' + sys.argv[1]

    render_image(imgpath=img_path)
