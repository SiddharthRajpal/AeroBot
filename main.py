import discord
import asyncio
from keep_alive import keep_alive
import urllib
import json
from googleapiclient.discovery import build
from replit import db
from discord.ext import commands
import random

client = commands.Bot(command_prefix =".")
client.remove_command("help")
mutelist = []
bad_words = [
  "kutta",
  "kamina"
]
db["y"] = True
youtube_id = "UCX6OQ3DkcsbYNE6H8uQQuVA"
@client.event
async def on_ready():
  print("Ready")

@client.command()
async def ping(ctx):
  await ctx.channel.send(f"{round(client.latency * 1000)} MS")

@client.command()
async def subs(ctx):
  
  api_key = #Hidden For Security Reasons
  youtube = build('youtube', 'v3', developerKey=api_key)

  request = youtube.channels().list(
  part='statistics',
  id=youtube_id
    )
  response = request.execute()
  #print(type(response))
  #print(response)
  x =response['items']
  y=x[0]
  u = y['statistics']
  await ctx.channel.send("Total subscriber count of AeroblazeYt:-")
  await ctx.channel.send("```"+u["subscriberCount"]+"```")

@client.command()
async def videos(ctx):
  api_key = #Hidden For Security Reasons
  youtube = build('youtube', 'v3', developerKey=api_key)

  request = youtube.channels().list(
  part='statistics',
  id=youtube_id
    )
  response = request.execute()
  #print(type(response))
  #print(response)
  x =response['items']
  y=x[0]
  u = y['statistics']
  #print(u)
  await ctx.channel.send("Total number of videos uploaded by Aeroblaze Yt:-")
  await ctx.channel.send("```"+u["videoCount"]+"```")

@client.command()
async def src(ctx):
  await ctx.channel.send("Source code available on github :- https://github.com/SiddharthRajpal/AeroBot")


@client.command()
async def mod(ctx,*,reason):
  await ctx.channel.send("Your mod application has been submittted and a moderator/admin will review it and contact you shortly.")
  mods = client.get_channel(842804602998226984)
  await mods.send(f"@{ctx.author} wants to be a moderator for the following reason :- **'{reason}'.** Please contact them and review their application.")

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question="None"):

  responses = [
  "As I see it, yes.", 
  "Ask again later.", 
  "Better not tell you now.", 
  "Cannot predict now.", 
  "Concentrate and ask again.",
  "Don’t count on it.", 
  "It is certain.", 
  "It is decidedly so.", 
  "Most likely.", 
  "My reply is no.", 
  "No",
  ""
  "My sources say no.",
  "Outlook not so good.", 
  "Outlook good.", 
  "Reply hazy, try again.", 
  "Signs point to yes.",
  "Very doubtful.", 
  "Without a doubt.",
  "Yes.", 
  "Yes – definitely.", 
  "You may rely on it."]
  await ctx.channel.send(f"```Question :- {question} \nAnswer :- {random.choice(responses)}``` ")


@client.command()
async def help(ctx):
  await ctx.channel.send(
      """         ```           AEROBOT BY RandomPotato
Welcome to this message. Aerobot is a custom bot that I have built specifically for this server using python. I will tell you about the commands and uses of Aerobot

.subs :- Sends the current subscribers of our youtube channel
.videos :- Sends the total number of videos uploaded to our youtube channel
.src :- view link for the source code
.help :- Get help
.8ball :- Ask a Question
.mod :- Request for moderator access (syntax = .mod reason)
If there are any suggestions or queries or bugs please feel free to DM me :)```""")
keep_alive()
client.run(#Hidden For security reasons)
