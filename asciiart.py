from PIL import Image, ImageDraw, ImageFont


class AsciiImage:
    '''Convert regular image to ascii image.'''
    image = None
    ascii_image = None
    ascii_data = []
    ascii_matrix = []
    min_size = 480
    font_size = 10
    chars = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjftI/\|)(1}{][?i!l-_+~;:,."^`'

    def generate(self, image_path):
        '''Return an ascii image of the image passed.'''
        self.image = Image.open(image_path)
        self._process_image()
        self._convert_data()
        self._reshape_data()
        self.ascii_image = self._create_ascii_image()
        return self.ascii_image

    def _process_image(self):
        '''Resize and greyscale the image.'''
        if self.min_size:
            # Resize large images cause they consume too much space and time.
            if self.image.width > self.min_size or self.image.height > self.min_size:
                self.image.thumbnail((self.min_size, self.min_size), Image.ANTIALIAS)

        # Convert image to black and white since it will be our reference to how dark or bright
        # each pixel.
        self.image = self.image.convert('L')

    def _convert_data(self):
        '''Convert image data to its ascii representation.'''
        image_data = list(self.image.getdata())

        for value in image_data:
            # Get the equivalent index of the current value in the character string.
            # Remember that when indexing is starts from 0 to length - 1.
            equivalence = round((value / 255) * len(self.chars)) - 1
            # We dont want negative index since it will point to the last character of the string.
            if equivalence < 0:
                equivalence = 0
            char = self.chars[equivalence]
            self.ascii_data.append(char)

    def _reshape_data(self):
        '''Reorganize ascii data from 1d to 2d list.'''
        for i in range(0, len(self.ascii_data), self.image.width):
            self.ascii_matrix.append(self.ascii_data[i:i + self.image.width])

    def _create_ascii_image(self):
        '''Return image drawn using the ascii data.'''
        size = (self.image.width * self.font_size, self.image.height * self.font_size)
        image = Image.new('RGB', size, color='WHITE')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('UbuntuMono-R.ttf', round(self.font_size * 1.5))

        posx = 0
        posy = 0

        for y in range(len(self.ascii_matrix)):
            for x in range(len(self.ascii_matrix[y])):
                draw.text((posx, posy), self.ascii_matrix[y][x], 'BLACK', font=font)

                posx += self.font_size

                if x >= len(self.ascii_matrix[y]) - 1:
                    posx = 0

            posy += self.font_size

        return image


if __name__ == '__main__':
    import sys

    ascii = AsciiImage()

    if '-q' in sys.argv:
        i = sys.argv.index('-q')
        quality = sys.argv[i + 1]

        if quality == 'low':
            ascii.min_size = 144
        elif quality == 'medium':
            ascii.min_size = 480
        elif quality == 'high':
            ascii.min_size = 720
        elif quality == 'normal':
            ascii.min_size = None
        else:
            raise SystemError('-q value must be low, medium, high, or normal.')

    if '-c' in sys.argv:
        i = sys.argv.index('-c')
        print(sys.argv[i + 1])
        ascii.chars = sys.argv[i + 1]

    image = ascii.generate(sys.argv[1])

    if '-d' in sys.argv:
        image.show()

    if '-o' in sys.argv:
        i = sys.argv.index('-o')
        path = sys.argv[i + 1]
        image.save(path)
