import discord
import os
import requests
import json
import random
from keep_alive import keep_alive



client = discord.Client() 

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  elif message.content.lower() == "*flip":
    toss = random.choice(["> It's __***TAILS***__","> It's __***HEADS***__"])
    await message.channel.send(toss)
  else:
    return

keep_alive()  

client.run(os.environ['TOKEN'])
