import discord

client = discord.Client()
client_token = 'NjczOTkwMTc0NTkzNjQ2NjIz.XkV3Jg.Azv5asgwBvGe0Xe22auvNDZx-Yk'
command_prefix = '>'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(command_prefix + 'bone'):
        await message.channel.send('I am the bone of my sword')


client.run(client_token)
