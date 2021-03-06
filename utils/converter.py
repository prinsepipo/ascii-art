from PIL import Image, ImageFont, ImageDraw


class ImageConverter:

    def __init__(self):
        self.input_divisor = 4
        self.output_multiplier = 8
        self._luminance = (0.2162, 0.7152, 0.0722)
        self.size = 16
        # It's up to you on what ascii characters to be rendered, this factor will affect the accuracy when rendering.
        # Here are some ascii-characters `^".,:;Il!i~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$
        self.characters = self.default_characters()
        self.filter = None

    def process_image(self, imgpath):
        img = Image.open(imgpath)

        # Lower the resolution of the image first to decrease processing time but
        # in return, accuracy will fluctuate dependently. Note that we do not rescale
        # low (but not so low) quality images.
        width, height = img.size
        if width > 1024 or height > 1024:
            w = width // self.input_divisor
            h = height // self.input_divisor
            img.thumbnail((w, h), Image.ANTIALIAS)
        width, height = img.size
        pixel_data = list(img.getdata())
        pixel_matrix = self.get_pixel_matrix(pixel_data, width, height)
        processed_matrix = self.get_processed_matrix(pixel_matrix)
        ascii_matrix = self.get_ascii_matrix(processed_matrix)

        # We multiply the width and height by 8 because when outputing the ascii characters
        # the size wont be the same as the pixel size.
        # Example: If the pixel at (0,0) is equivalent to `@` then we render it as a 16px size
        # font because if it is 1px then it will just show a block or a pixel dot not the `@` itself.
        output = self.create_image(
            ascii_matrix, width * self.output_multiplier, height * self.output_multiplier)
        return output

    def get_pixel_matrix(self, pixel_data, width, height):
        """
        The pixel data should be divided as rows (i.e. matrix[[row1...], [row2...], [row3...] ...])
        to simulate an image which has width and height. We use this method because the image data
        is just a single list, we want a 2d array not 1d.
        """
        pixel_matrix = []
        for i in range(0, width * height, width):
            pixel_matrix.append(pixel_data[i: i + width])

        return pixel_matrix

    def get_processed_matrix(self, pixel_matrix):
        processed_matrix = []

        for x in range(len(pixel_matrix)):
            row = []
            for y in range(len(pixel_matrix[x])):
                pixel = pixel_matrix[x][y]
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                value = None

                if self.filter == 'luminosity':
                    # General formula for gettig the luminance of a color.
                    # There are many formula for getting the luminance of a color depending on the accuarcy you are targeting.
                    #  https://en.wikipedia.org/wiki/Luma_(video) read here for more information.
                    value = (
                        r * self._luminance[0]) + (g * self._luminance[1]) + (b * self._luminance[2])
                elif self.filter == 'lightness':
                    value = (max(r, g, b) + min(r, g, b)) // 2
                else:
                    value = (r + g + b) // 3

                row.append(value)

            processed_matrix.append(row)

        return processed_matrix

    def get_ascii_matrix(self, processed_matrix):
        ascii_matrix = []

        for x in range(len(processed_matrix)):
            line = []
            for y in range(len(processed_matrix[x])):
                equivalence = (
                    processed_matrix[x][y] / 255) * len(self.characters)
                line.append(self.characters[int(equivalence) - 1])
            ascii_matrix.append(line)

        return ascii_matrix

    def create_image(self, ascii_matrix, width, height):
        img = Image.new('RGB', (width, height), 'WHITE')
        draw = ImageDraw.Draw(img)

        posx = 0
        posy = 0
        for y in range(len(ascii_matrix)):
            for x in range(len(ascii_matrix[y])):
                draw.text((posx, posy), ascii_matrix[y][x], (0, 0, 0))

                posx += self.size // 2

                if x == len(ascii_matrix[y]) - 1:
                    posx = 0

            posy += self.size // 2

        return img

    def default_characters(self):
        return "`^\".,:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
