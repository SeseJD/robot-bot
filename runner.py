import discord
from discord.ext import commands

import asyncio
import os

pr = '_'
client = commands.Bot(command_prefix = pr)

cogs = ['slowmode']

@client.event
async def on_ready():
  print('Bot ready!')
  playing = discord.Game('Bounty Hunters')
  await client.change_presence(status=discord.Status.online, activity = playing)

if __name__ == '__main__':
  for cog in cogs:
    try:
      client.load_extension(cog)
      print('Cog {} loaded'.format(cog))
    except Exception as error:
      print('Cog {} failed to load because: [{}]'.format(cog, error))

client.run(os.getenv('BOT_TOKEN'))
