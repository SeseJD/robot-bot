import discord
from discord.ext import commands
from discord.ext.commands import Bot

import asyncio
import os
import random

client = discord.Client()
_client = commands.Bot(command_prefix = ';')

admin = 422126708003438592

key_type = {
  'Major', 'Minor'
}

key = {
  'A', 'B', 'C', 'D', 'E', 'F', 'G'
}

@client.event
async def on_ready():
  print('Bot ready!')


@client.event
async def on_message(message):
  if message.content.startswith(';owner'):
    await client.send_message(message.channel, 'This bot was 100% created by Sese#1078. Cheers to him!')
  if message.content.startswith(';channelinfo'):
    await client.send_message(message.channel, '```{}```'.format(message.channel.topic))
  if message.content.startswith(';ranmusickey'):
    await client.send_message(message.channel, '{} {}'.format(random.choice(key), random.choice(key_type)))


client.run(os.getenv('BOT_TOKEN'))
