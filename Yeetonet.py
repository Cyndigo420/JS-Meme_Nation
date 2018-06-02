import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "js!")
@client.event
async def on_ready():
    print("Developed by Cyndigo#5449")
    await client.change_presence(game=discord.Game(name"js!help"))

@client.event
async def on_message(message):
    if message.content.startswith('Yeet')
    msg = 'Yeet'.format(message)
    await client.send_message(message.channel, msg)

client.run(os.getenv('TOKEN'))
