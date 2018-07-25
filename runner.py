import discord
from discord.ext import commands
from discord.ext.commands import Bot

import asyncio

client = discord.Client()

@client.event
async def on_ready():
  print('Bot ready!')

@client.event
async def on_message(message):
  if message.content.startswith(';owner'):
    await client.send_message(message.channel, 'This bot was 100% created by Sese#1078. Cheers to him!')
  if message.content.startswith(';channelinfo'):
    await client.send_message(message.channel, '```{}```'.format(message.channel.topic))
    
client.run('token')
