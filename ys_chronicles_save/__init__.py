# imports
from io import BytesIO
from os.path import isfile
from PIL import Image
from struct import pack, unpack

# class to represent Ys I & II Chronicles+ save files
class Save:
    # constructor
    def __init__(self, path):
        if not isinstance(path, str) or not path.endswith('.bmp') or not isfile(path):
            raise ValueError("Invalid save: %s")
        raw_data = open(path, 'rb').read()
        bmp_size = unpack('<I', raw_data[2:6])[0]
        self.bmp_data = raw_data[:bmp_size]
        self.save_data = raw_data[bmp_size:]

    # show the BMP image of this save
    def show_image(self):
        img = Image.open(BytesIO(self.bmp_data))
        img.show()

    # print a summary of this save
    def print_summary(self, show_image=True):
        if show_image:
            self.show_image()