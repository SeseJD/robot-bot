import discord
from discord.ext import commands
from discord.ext.commands import Bot

import asyncio
import os

client = discord.Client()
_client = commands.Bot(command_prefix = ';')

admin = 422126708003438592

@_client.event
async def on_ready():
  print('Bot ready!')

"""
@_client.event
async def on_message(message):
  if message.content.startswith(';owner'):
    await client.send_message(message.channel, 'This bot was 100% created by Sese#1078. Cheers to him!')
  if message.content.startswith(';channelinfo'):
    await client.send_message(message.channel, '```{}```'.format(message.channel.topic))
"""
      

@_client.command()
async def clear(context, amount=100):
  if context.message.author.id == admin:
    msgs = []
    async for msg in _client.logs_from(context.message.channel, limit = int(amount) + 1):
      msgs.append(msg)
    await _client.delete_messages(msgs)
    
_client.run(os.getenv('BOT_TOKEN'))
