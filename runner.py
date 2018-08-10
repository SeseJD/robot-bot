import discord
from discord.ext import commands

import asyncio
import os

pr = '_'
client = commands.Bot(command_prefix = pr)

playing = discord.Game('Bounty Hunters')

cogs = ['slowmode']

@client.event
async def on_ready():
  print('Bot ready!')
  await client.change_presence(activity = playing)

if __name__ == '__main__':
  for cog in cogs:
    try:
      client.load_extension(cog)
      print('Cog {} loaded'.format(cog))
    except Exception as error:
      print('Cog {} failed to load because: [{}]'.format(cog, error))

client.run(os.getenv('BOT_TOKEN'))
