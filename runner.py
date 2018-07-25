import discord
from discord.ext import commands
from discord.ext.commands import Bot

import asyncio
import time
import os

@client.event
async def on_ready():
  print('Bot ready!')

@client.event
async def on_message(message):
  if message.content.startswith(';help'):
    
