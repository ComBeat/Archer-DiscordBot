import os
from random import randint

import discord


def image():
    dir_path = 'img/'
    nr_of_items = len(os.listdir(dir_path))
    img_path = dir_path + 'rin' + str(randint(0, nr_of_items - 1)) + '.png'

    return discord.File(img_path)
