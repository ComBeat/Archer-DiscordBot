import json
import logging
from io import FileIO

import discord

# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
# TODO Use sys/os funcs to specify log path
handler = logging.FileHandler(filename='../archer.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Essential stuff like token and so on
auth_file = FileIO('../auth.json', mode='r')
json_object = json.load(auth_file)
bot_token = json_object['bot_token']
dev_id = int(json_object['dev_id'])
dev_command_prefix = json_object['dev_command_prefix']
auth_file.close()
client = discord.Client()
command_prefix = '>'

# Not so essential stuff
bot_activity = discord.Activity(name='EMIYA', type=discord.ActivityType.listening)
dev_user = None
chant = 'I am the bone of my sword\n' \
      'Steel is my body and fire is my blood\n' \
      'I have created over a thousand blades\n' \
      'Unknown to Death,\n' \
      'Nor known to Life.\n' \
      'Have withstood pain to create many weapons\n' \
      'Yet, those hands will never hold anything\n' \
      'So as I pray, Unlimited Blade Works.'


@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))
    global dev_user
    dev_user = client.get_user(dev_id)
    await client.change_presence(activity=bot_activity)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(command_prefix + 'chant'):
        await message.channel.send(chant)

    elif message.content.startswith(command_prefix + 'rin'):
        await message.add_reaction('<:rin0:680184904415445045>')
        await message.add_reaction('\N{THINKING FACE}')
        await message.channel.send('<:rin0:680184904415445045>')  # Format to post emoji

    elif message.content.startswith(command_prefix + 'dm'):
        await message.author.send('Hello world')

    elif message.content.startswith(command_prefix + 'embed'):
        embed = discord.Embed(title='Unlimited Blade Works', color=discord.Colour.red())
        await message.channel.send(embed=embed)

    # TODO 'emiya' -> go to voice and play EMIYA

    if message.content.startswith(dev_command_prefix + 'ping') and message.author == dev_user:
        await message.channel.send('You are the bone of my sword')
        await message.channel.send(dev_command_prefix + 'ping')
        return
    else:
        return


client.run(bot_token)
