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

key_type = {
  'Major', 'Minor'
}

key = {
  'A', 'B', 'C', 'D', 'E', 'F', 'G'
}

directory = os.getcwd()
os.chdir(directory)

@client.event
async def on_ready():
  print('Bot ready!')
  print(directory)

@client.event
async def on_message(message):
  with open('users.json', 'r') as f:
    users = json.load(f)
  
  await update_data(users, message.author)
  await add_experience(users, message.author, 20)
  await level_up(users, message.author, message.channel)
  
  
  with open('users.json', 'w') as f:
    json.dump(users, f)
  
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
  await client.edit_channel_permissions(message.channel, message.author, slowmodeoff)

# Credit to Lucas Kumara's level up tutorial
async def update_data(users, user):
  if not user.id in users:
    users[user.id] = {}
    users[user.id]['xp'] = 0
    users[user.id]['level'] = 0

async def add_experience(users, user, xp):
  users[user.id]['xp'] += xp

async def level_up(users, user, channel):
  xp = users[user.id]['xp']
  lvl_start = users[user.id]['level']
  lvl_end = int(xp ** (1/4))
  
  if lvl_start < lvl_end:
    await client.send_message(channel, '{}, you gained up to **level {}**! Keep it up!'.format(user.mention, lvl_end))
    users[user.id]['level'] = lvl_end

client.run(os.getenv('BOT_TOKEN'))
