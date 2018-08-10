import discord
from discord.ext import commands

import os

prefix = '_'
client = discord.Client()

client.run(os.getenv('BOT_TOKEN'))
