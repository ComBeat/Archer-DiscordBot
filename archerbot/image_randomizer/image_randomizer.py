import os
from random import randint

import discord


def image():
    dir_path = '../img/'
    nr_of_items = len(os.listdir(dir_path))
    # img_nr = randint(0, nr_of_items - 1)
    img_path = dir_path + 'rin' + str(randint(0, nr_of_items - 1)) + '.png'
    img = discord.File(img_path)

    return img


class ImageRandomizer:
    # def __init__(self):

    # @staticmethod
    pass
