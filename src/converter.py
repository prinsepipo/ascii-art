from PIL import Image, ImageFont, ImageDraw


def render_image(imgpath):
    ascii_image = process_image(imgpath)
    ascii_image.show()


def process_image(imgpath):
    IMG_FILE = imgpath
    img = Image.open(IMG_FILE)

    # Lower the resolution of the image first to decrease processing time but
    # in return, accuracy will fluctuate dependently.
    width, height = img.size
    img.thumbnail((width // 4, height // 4), Image.ANTIALIAS)
    width, height = img.size
    pixel_data = list(img.getdata())
    pixel_matrix = get_pixel_matrix(pixel_data, width, height)
    luminance_matrix = get_luminance_matrix(pixel_matrix)
    ascii_matrix = convert_to_ascii(luminance_matrix)

    # We multiply the width and height by 8 because when outputing the ascii characters
    # the size wont be the same as the pixel size.
    # Example: If the pixel at (0,0) is equivalent to `@` then we render it as a 16px size
    # font because if it is 1px then it will just show a block or a pixel dot not the `@` itself.
    output = create_image(ascii_matrix, width * 8, height * 8)
    return output


def get_pixel_matrix(pixel_data, width, height):
    # The pixel data should be divided as rows (i.e. matrix[[row1...], [row2...], [row3...] ...])
    # to simulate an image which has width and height. We use this method because the image data
    # is just a single list, we want a 2d array not 1d.
    pixel_matrix = []
    total_pixels = width * height
    for i in range(0, total_pixels, width):
        pixel_matrix.append(pixel_data[i: i + width])

    return pixel_matrix


def get_luminance_matrix(pixel_matrix):
    luminance_matrix = []

    for x in range(len(pixel_matrix)):
        row = []
        for y in range(len(pixel_matrix[x])):
            # We use the general formula for gettig the luminace (or brightness, but not the right word) of a color.
            # There are many formula for getting the luminance of a color depending on the accuarcy you are targeting.
            #  https://en.wikipedia.org/wiki/Luma_(video) read here for more information.
            r, g, b = pixel_matrix[x][y]
            luminance = 0.2162 * r + 0.7152 * g + 0.0722 * b
            row.append(luminance)
        luminance_matrix.append(row)

    return luminance_matrix


def convert_to_ascii(luminance_matrix):
    # It's up to you on what ascii characters to be rendered, this factor will affect the accuracy when rendering.
    # Here are some ascii-characters `^".,:;Il!i~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$
    ascii_char = "`^$@"

    ascii_matrix = []

    for x in range(len(luminance_matrix)):
        line = []
        for y in range(len(luminance_matrix[x])):
            equivalence = (luminance_matrix[x][y] / 255) * len(ascii_char)
            line.append(ascii_char[int(equivalence) - 1])
        ascii_matrix.append(line)

    return ascii_matrix


def create_image(ascii_matrix, width, height):
    img = Image.new('RGB', (width, height), 'WHITE')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('UbuntuMono-R.ttf', 16)

    posx = 0
    posy = 0
    for y in range(len(ascii_matrix)):
        for x in range(len(ascii_matrix[y])):
            draw.text((posx, posy), ascii_matrix[y][x], (0, 0, 0), font)
            posx += 8

            if x == len(ascii_matrix[y]) - 1:
                posx = 0

        posy += 8

    img.save('image/output.png', 'PNG')
    return img
