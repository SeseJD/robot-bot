import discord
from discord.ext import commands
from discord.ext.commands import Bot

import asyncio
import os

client = discord.Client()
_client = commands.Bot(command_prefix = ';')

admin = 471184662119710720

@client.event
async def on_ready():
  print('Bot ready!')

@client.event
async def on_message(message):
  if message.content.startswith(';owner'):
    await client.send_message(message.channel, 'This bot was 100% created by Sese#1078. Cheers to him!')
  if message.content.startswith(';channelinfo'):
    await client.send_message(message.channel, '```{}```'.format(message.channel.topic))
      

client.command(pass_context = True)
async def clear(context, ammount=100):
  perms = context.message.channel.permissions_for(context.message.author)
  async for perm in perms:
    if perm = 11:
      msgs = []
      async for msg in _client.logs_from(context.message.channel, limit = amount):
        msgs.append(msg)
      await _client.delete_messages(msgs)
    
client.run(os.getenv('BOT_TOKEN'))
