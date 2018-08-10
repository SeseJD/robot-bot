import discord
from discord.ext import commands

import asyncio
import os
import time

slowmodeon = discord.PermissionOverwrite(send_messages = False)
slowmodeoff = discord.PermissionOverwrite()

class Slowmode:
  def __init__(self, client):
    self.client = client
  
  @client.event
  async def on_message(message):
    await client.edit_channel_permissions(message.channel, message.author, slowmodeon)
    time.sleep(4)
    await client.edit_channel_permissions(message.channel, message.author, slowmodeoff)
  
def setup(Client):
  client.add_cog(Slowmode(client)))
