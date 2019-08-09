from PIL import Image
import time


def get_pixel_matrix(pixel_data, width, height):
    return [pixel_data[n:n+width] for n in range(0, width * height, width)]


def get_brightness_matrix(pixel_matrix, width, height):
    brightness_matrix = []

    for x in range(height):
        layer = []
        for y in range(width):
            brightness = sum(pixel_matrix[x][y]) // 3
            layer.append(brightness)
        brightness_matrix.append(layer)

    return brightness_matrix


def get_ascii_image(brightness_matrix, width, height):
    ascii_char = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    lines = []

    for x in range(height):
        line = ''
        for y in range(width):
            v = (brightness_matrix[x][y] / 255) * 64
            line += ascii_char[int(v)]
        lines.append(line)

    return '\n'.join(lines)


def process_image(imgpath):
    IMG_FILE = imgpath
    img = Image.open(IMG_FILE)
    img = img.resize((258, 258), Image.ANTIALIAS)
    width, height = img.size
    pixel_data = list(img.getdata())
    pixel_matrix = get_pixel_matrix(pixel_data, width, height)
    brightness_matrix = get_brightness_matrix(pixel_matrix, width, height)
    ascii_image = get_ascii_image(brightness_matrix, width, height)
    return ascii_image


def render_image(imgpath):
    ascii_image = process_image(imgpath)
    print(ascii_image)
