import discord
from discord.ext import commands
from discord.ext.commands import Bot

import asyncio
import os
import random

prefix = '_'

client = discord.Client()
_client = commands.Bot(command_prefix = '{}'.format(prefix))

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
  await client.send_message(468145561233784834, 'I am now updated!')


@client.event
async def on_message(message):
  if message.content.startswith('{}owner'.format(prefix)):
    await client.send_message(message.channel, 'This bot was 100% created by Sese#1078. Cheers to him!')
  if message.content.startswith('{}channelinfo'.format(prefix)):
    await client.send_message(message.channel, '```{}```'.format(message.channel.topic))
  if message.content.startswith('{}ranmusickey'.format(prefix)):
    await client.send_message(message.channel, '{} {}'.format(random.choice(key), random.choice(key_type)))
  if message.content.startswith('no u'):
    await client.send_message(message.channel, 'No... u')


client.run(os.getenv('BOT_TOKEN'))
