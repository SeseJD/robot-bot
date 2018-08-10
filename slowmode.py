import discord
from discord.ext import commands

import asyncio
import os
import time

client = commands.Bot(command_prefix = '_')
CL = discord.Client()

slowmodeon = discord.PermissionOverwrite(send_messages = False)
slowmodeoff = discord.PermissionOverwrite()

class Slowmode:
  def __init__(self, Client):
    self.client = Client
  
  @CL.event
  async def on_message(message):
    print('New msg')
    await CL.edit_channel_permissions(message.channel, message.author, slowmodeon)
    time.sleep(4)
    await CL.edit_channel_permissions(message.channel, message.author, slowmodeoff)
  
def setup(Client):
  client.add_cog(Slowmode(Client))
