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
  await client.change_presence(game = discord.Game(name = 'Bounty Hunters'))

@client.event
async def on_message(message):
  if message.content.startswith('{}help'.format(prefix)):
    await client.send_message(message.channel,"""
    ```
    The prefix is {}
    
    help - To get info about all the commands
    info - All about me!
    channelinfo - To get more information about this channel.
    ranmusickey - A random music key generator
    slowmode - All you need to know about slowmode
    ```
    """.format(prefix))
  if message.content.startswith('{}info'.format(prefix)):
    await client.send_message(message.channel, 'This bot was 100% created by Sese#1078. For more info about Hunterbot, please check https://github.com/SeseJD/robot-bot')
  if message.content.startswith('{}channelinfo'.format(prefix)):
    await client.send_message(message.channel, '```{}```'.format(message.channel.topic))
  if message.content.startswith('{}ranmusickey'.format(prefix)):
    await client.send_message(message.channel, '{} {}'.format(random.choice(key), random.choice(key_type)))
  if message.content.startswith('{}slowmode'.format(prefix)):
    await client.send_message(message.channel, 'This server uses a 2 second **slowmode** for every channel. It will temporarily mute you from the specific channel then unmute after the 2 seconds.')
  if message.content.startswith('no u') or message.content.startswith('No u') or message.content.startswith('No you'):
    await client.send_message(message.channel, 'No... u')
  try:
    await client.edit_channel_permissions(message.channel, message.author, slowmode)
    time.sleep(2)
    await client.edit_channel_permissions(message.channel, message.author, slowmodeoff)
  except:
    print('slowmode disabled :(')

client.run(os.getenv('BOT_TOKEN'))
