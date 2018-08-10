import discord
from discord.ext import commands

import asyncio
import os

slowmodeon = discord.PermissionOverwrite(send_messages = False)
slowmodeoff = discord.PermissionOverwrite()

class Slowmode:
  def __init__(self, client):
    self.client = client
  
  @client.event
  async def on_message(message):
    
  
def setup(client):
  client.add_cog(Slowmode(client)))
