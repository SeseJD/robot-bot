import discord
from discord.ext import commands

import asyncio
import os

pr = '_'
client = discord.Client()

cogs = [']

@client.event
async def on_ready():
  print('Bot ready!')

if __name__ == '__main__':
  for cog in cogs:
    try:
      client.load_extension(cog)
    except Exception as error:
      print('Cog {} failed to load because: [{}]'.format(cog, error))

client.run(os.getenv('BOT_TOKEN'))
