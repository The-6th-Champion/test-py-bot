import discord
import os
import asyncio

from discord.ext import commands

client = commmands.Bot(command_prefix="!")

@client.event
async def on_ready():
  print("starting")
  asyncio.sleep(5)
  send_to =  client.get_channel(781215248790978601)
  await send_to.send("Im alive i think")

@client.command()
async def hi(ctx):
  await ctx.send("\'sup")
  
client.run(os.environ.get("TOKEN"))
