import discord
import json
from io import FileIO

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
