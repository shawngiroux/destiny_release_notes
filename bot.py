import discord
import asyncio
from main import get_release_notes

client = discord.Client()

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith('!sleep'):
        yield from asyncio.sleep(5)
        yield from client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!die'):
        yield from client.send_message(message.channel, 'So long dear friends..')
        yield from client.logout()
    elif message.content.startswith('!notes'):
        notes = get_release_notes('https://www.bungie.net/en/Explore/Detail/Update/46472')
        em = discord.Embed(title='My Embed Title', description=notes, colour=0xDEADBF)
        yield from client.send_message(message.channel, embed=em)

client.run('token')