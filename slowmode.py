import discord
from discord.ext import commands

import asyncio
import os
import time

slowmodeon = discord.PermissionOverwrite(send_messages = False)
slowmodeoff = discord.PermissionOverwrite()

class Slowmode:
  def __init__(self, Client):
    self.client = Client
  
  @client.event
  async def on_message(message):
    print('New msg')
    await client.edit_channel_permissions(message.channel, message.author, slowmodeon)
    time.sleep(4)
    await client.edit_channel_permissions(message.channel, message.author, slowmodeoff)
  
def setup(client):
  client.add_cog(Slowmode(client))
