import discord
from discord.ext import commands

import asyncio
import os
import time

DCclient = discord.Client()

slowmodeon = discord.PermissionOverwrite(send_messages = False)
slowmodeoff = discord.PermissionOverwrite()

class Slowmode:
  def __init__(self, client):
    self.client = client
  
  @DCclient.event
  async def on_message(message):
    await DCclient.edit_channel_permissions(message.channel, message.author, slowmodeon)
    time.sleep(4)
    await DCclient.edit_channel_permissions(message.channel, message.author, slowmodeoff)
  
def setup(client):
  client.add_cog(Slowmode(client)))
