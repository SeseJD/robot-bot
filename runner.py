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


@_client.event
async def on_message(message):
  if message.content.startswith(';owner'):
    await client.send_message(message.channel, 'This bot was 100% created by Sese#1078. Cheers to him!')
  if message.content.startswith(';channelinfo'):
    await client.send_message(message.channel, '```{}```'.format(message.channel.topic))


_client.run(os.getenv('BOT_TOKEN'))
