import discord
from discord.ext import commands
from discord.ext.commands import Bot

import asyncio
import os

client = discord.Client()
_client = commands.Bot(command_prefix = ';')

admin = 422126708003438592

@client.event
async def on_ready():
  print('Bot ready!')

@client.event
async def on_message(message):
  if message.content.startswith(';owner'):
    await client.send_message(message.channel, 'This bot was 100% created by Sese#1078. Cheers to him!')
  if message.content.startswith(';channelinfo'):
    await client.send_message(message.channel, '```{}```'.format(message.channel.topic))
  
  if admin = message.author.id:
    if message.content.startswith(';kick'):
      
    
client.command(pass_context = True)
async def clear(context, ammount=100):
  if admin = message.author.id:
    msgs = []
    async for msg in _client.logs_from(context.message.channel, limit = amount):
      msgs.append(msg)
    await _client.delete_messages(msgs)
    ms = await _client.say(':ok_hand: deleted messages for ya')
    
client.run(os.getenv('BOT_TOKEN'))
