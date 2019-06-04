from PIL import Image
import time


def get_pixel_matrix(pixel_data):
    global width, height
    return [pixel_data[n:n+width] for n in range(0, width * height, width)]


def get_brightness_matrix(pixel_matrix):
    global width, height
    brightness_matrix = []

    for x in range(height):
        layer = []
        for y in range(width):
            brightness = sum(pixel_matrix[x][y]) // 3
            layer.append(brightness)
        brightness_matrix.append(layer)

    return brightness_matrix


def get_ascii_image(brightness_matrix):
    global width, height

    lines = []

    for x in range(height):
        line = ''
        for y in range(width):
            v = (brightness_matrix[x][y] / 255) * 64
            line += ascii_char[int(v)]
        lines.append(line)

    # return '\n'.join(lines)
    return lines


IMG_FILE = 'image/003.jpg'
SIZE = (400, 225)
img = Image.open(IMG_FILE)
img = img.resize(SIZE)
width, height = img.size
pixel_data = list(img.getdata())
pixel_matrix = get_pixel_matrix(pixel_data)
brightness_matrix = get_brightness_matrix(pixel_matrix)
ascii_char = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_image = get_ascii_image(brightness_matrix)

# print(ascii_image)

for line in ascii_image:
    time.sleep(0.3)
    print(line)
