import json
import logging
from io import FileIO

import discord

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
# TODO Use sys/os funcs to specify log path
handler = logging.FileHandler(filename='../archer.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# TODO Use sys/os funcs to locate auth file
auth_file = FileIO('../auth.json', mode='r')
bot_token = json.load(auth_file)['bot_token']
client = discord.Client()
command_prefix = '>'


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(command_prefix + 'bone'):
        await message.channel.send('I am the bone of my sword')


client.run(bot_token)
