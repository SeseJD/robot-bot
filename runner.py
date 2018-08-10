import discord
from discord.ext import commands
from discord.ext.commands import Bot

import asyncio
import json
import os
import random
import time

slowmode = discord.PermissionOverwrite()
slowmode.send_messages = False


slowmodeoff = discord.PermissionOverwrite()

prefix = '_'

client = discord.Client()
_client = commands.Bot(command_prefix = '{}'.format(prefix))

admin = 422126708003438592

key_type = ['Major', 'Minor']

key = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

@client.event
async def on_ready():
  print('Bot ready!')
  print(directory)
  await client.change_presence(game = discord.Game(name = 'Bounty Hunters'))

@client.event
async def on_message(message):
  if message.channel.name == 'announcements':
    message.add_reaction(emoji = discord.Emoji(name = 'ok_hand'))
  if message.content.startswith('{}owner'.format(prefix)):
    await client.send_message(message.channel, 'This bot was 100% created by Sese#1078. Cheers to him!')
  if message.content.startswith('{}channelinfo'.format(prefix)):
    await client.send_message(message.channel, '```{}```'.format(message.channel.topic))
  if message.content.startswith('{}ranmusickey'.format(prefix)):
    await client.send_message(message.channel, '{} {}'.format(random.choice(key), random.choice(key_type)))
  if message.content.startswith('no u') or message.content.startswith('No u') or message.content.startswith('No you'):
    await client.send_message(message.channel, 'No... u')
  await client.edit_channel_permissions(message.channel, message.author, slowmode)
  time.sleep(4)
  await client.edit_channel_permissions(message.channel, message.author, Overwrite = None)

client.run(os.getenv('BOT_TOKEN'))
