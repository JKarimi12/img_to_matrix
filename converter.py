from copy import deepcopy

from PIL import Image
import numpy as np


class Converter:

    def __init__(self):
        self.path = None
        self.red_channel = None
        self.green_channel = None
        self.blue_channel = None
        self.rgb_matrix = None

    def input_image(self, path):
        self.path = path
        try:
            image = Image.open(self.path, 'r')
            self.rgb_matrix = np.asarray(image)
            for i, field_name in enumerate(['red_channel', 'green_channel', 'blue_channel']):
                matrix = deepcopy(self.rgb_matrix)
                exclude_channels = {0, 1, 2} - {i}
                for channel in exclude_channels:
                    matrix[:, :, channel] = 0
                setattr(self, field_name, matrix)
            self.__show_channel_images()
            self.__show_custom_gray_image()
            self.__show_real_gray_image(image)
        except FileNotFoundError:
            print('File not found')

    def __show_channel_images(self):
        for channel in ['red_channel', 'green_channel', 'blue_channel']:
            Image.fromarray(getattr(self, channel)).show(channel)

    def __show_custom_gray_image(self):
        r_matrix = self.red_channel[:, :, 0]
        g_matrix = self.red_channel[:, :, 1]
        b_matrix = self.red_channel[:, :, 2]
        gray_matrix = (r_matrix + g_matrix + b_matrix) / 3
        Image.fromarray(gray_matrix).show('custom gray image')

    def __show_real_gray_image(self, image):
        image.convert('L').show('real gray image')

