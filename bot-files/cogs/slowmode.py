import discord
from discord.ext import commands

import asyncio
import os
import time

slowmodeon = discord.PermissionOverwrite(send_messages = False)
slowmodeoff = discord.PermissionOverwrite()

class Slowmode:
  def __init__(self, client):
    self.client = Client
  
  @client.event
  async def on_message(message):
    await Client.edit_channel_permissions(message.channel, message.author, slowmodeon)
    time.sleep(4)
    await Client.edit_channel_permissions(message.channel, message.author, slowmodeoff)
  
def setup(Client):
  Client.add_cog(Slowmode(Client)))
