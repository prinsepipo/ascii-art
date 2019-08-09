import os

from src.converter import render_image


def get_images():
    return os.listdir('image')


if __name__ == "__main__":
    imgs = get_images()

    for img in imgs:
        imgpath = 'image/' + img
        render_image(imgpath)
        print('\n')
