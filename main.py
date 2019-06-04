from PIL import Image


IMG_FILE = 'image/003.jpg'

img = Image.open(IMG_FILE)
img = img.resize((400, 225))
width, height = img.size
pixel_data = list(img.getdata())
pixel_matrix = [pixel_data[n:n+width] for n in range(0, width * height, width)]
brightness_matrix = []

for x in range(height):
    layer = []
    for y in range(width):
        brightness = sum(pixel_matrix[x][y]) // 3
        layer.append(brightness)
    brightness_matrix.append(layer)

ascii_char = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
lines = []

for x in range(height):
    line = ''
    for y in range(width):
        v = (brightness_matrix[x][y] / 255) * 64
        line += ascii_char[int(v)]
    lines.append(line)

ascii_image = '\n'.join(lines)

print(ascii_image)
