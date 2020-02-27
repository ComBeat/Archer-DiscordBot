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
client = discord.Client(status=discord.Status.dnd)
command_prefix = '>'


@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))
    print('Guilds: {0}'.format(client.guilds))
    print('Emojis: {0}'.format(client.emojis))
    print('Users: {0}'.format(client.users))


@client.event
async def on_message(message):
    if message.author == client.user:
        # await message.channel.send(discord.emoji.Emoji.id(680184904415445045))
        return

    if message.content.startswith(command_prefix + 'chant'):
        await message.channel.send('I am the bone of my sword\n'
                                   'Steel is my body and fire is my blood\n'
                                   'I have created over a thousand blades\n'
                                   'Unknown to Death,\n'
                                   'Nor known to Life.\n'
                                   'Have withstood pain to create many weapons\n'
                                   'Yet, those hands will never hold anything\n'
                                   'So as I pray, Unlimited Blade Works.')

    elif message.content.startswith(command_prefix + 'rin'):
        await message.add_reaction('<:rin0:680184904415445045>')
        await message.channel.send('<:rin0:680184904415445045>')  # Format to post emoji


# class Archer(discord.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))
#         print('Guilds: {0}'.format(self.guilds))
#         print('Emojis: {0}'.format(self.emojis))
#         print('Users: {0}'.format(self.users))
#
#     async def on_message(self, message):
#         if message.author == self.user:
#             # await message.channel.send(discord.emoji.Emoji.id(680184904415445045))
#             return
#
#         if message.content.startswith(command_prefix + 'chant'):
#             await message.channel.send('I am the bone of my sword\n'
#                                        'Steel is my body and fire is my blood\n'
#                                        'I have created over a thousand blades\n'
#                                        'Unknown to Death,\n'
#                                        'Nor known to Life.\n'
#                                        'Have withstood pain to create many weapons\n'
#                                        'Yet, those hands will never hold anything\n'
#                                        'So as I pray, Unlimited Blade Works.')
#
#
# client = Archer()
client.run(bot_token)
