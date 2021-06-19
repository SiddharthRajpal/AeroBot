import discord
import asyncio
from keep_alive import keep_alive
from replit import db
import urllib
import json
from googleapiclient.discovery import build
from discord.ext import commands
client=discord.Client()
mutelist = []
bad_words = [
  "kutta",
  "kamina"
]
db["y"]=True


@client.event
async def on_ready():
  print("Ready")
  await client.change_presence(activity=discord.Game(name=" .help"))

@client.event
async def on_message(message):
  youtube_id = "UCX6OQ3DkcsbYNE6H8uQQuVA"

  if message.author == client.user:
    return
  msg=message.content
  waitTime=300 
  if message.author in mutelist:
    await message.delete()
  if any(word in msg.lower() for word in bad_words) and db["y"]==True:
    await message.delete()
    mutelist.append(message.author)
    await message.channel.send(f"{message.author} just said a bad word :angry: :triumph:")
    await asyncio.sleep(1)
    await message.channel.send(f"{message.author} has been muted in this server for 5 minutes")
    await asyncio.sleep(waitTime)
    mutelist.remove(message.author)
    mutelist.remove(message.author)
    await message.channel.send(f"** Mute for {message.author} has ended you may speak again**")
  if msg.startswith(".offcheck"):
  
    db["y"]=False
    await message.channel.send("BadWordCheck is now off")
  if msg.startswith(".oncheck"):
    
    db["y"]=True
    await message.channel.send("BadWordCheck is now on")

  if message.author in mutelist and msg.startswith(#Hidden for server security):
    mutelist.remove(message.author)
    await message.channel.send(f"{message.author} has been unmuted for saying the secret word!!")
    #From Line no 19-38 is BadWordCheck
  if msg.startswith(".subs"):
    api_key = #Hidden for security purposes
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.channels().list(
        part='statistics',
        id=youtube_id
    )

    response = request.execute()
    print(type(response))
    print(response)
    x =response['items']
    y=x[0]
    u = y['statistics']
    await message.channel.send("Total subscriber count of AeroblazeYt:-")
    await message.channel.send("```"+u["subscriberCount"]+"```")
  if msg.startswith(".videos"):
    api_key = #Hidden For Security Purposes
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.channels().list(
        part='statistics',
        id=youtube_id
    )

    response = request.execute()
    print(type(response))
    print(response)
    x =response['items']
    y=x[0]
    u = y['statistics']
    print(u)
    await message.channel.send("Total number of videos uploaded by Aeroblaze Yt:-")
    await message.channel.send("```"+u["videoCount"]+"```")
  if msg.startswith(".mod"):
      await message.channel.send("Your mod application has been submittted and a moderator/admin will review it and contact you shortly.")
      mods = client.get_channel(842804602998226984)
      await mods.send(f"{message.author} wants to be a moderator please contact them.")
      

  if msg.startswith(".src"):
    await message.channel.send("Source code available on github :- https://github.com/SiddharthRajpal/AeroBot")
  if msg.startswith(".help"):
    await message.channel.send(
      """         ```                          AEROBOT BY RandomPotato
Welcome to this message. Aerobot is a custom bot that I have built specifically for this server using python. I will tell you about the commands and uses of Aerobot

.subs :- Sends the current subscribers of our youtube channel
.videos :- Sends the total number of videos uploaded to our youtube channel

There is a constant check on bad words in this server via Aerobot, if you use any bad word you will be muted for 5 minutes

.offcheck :- turns BadWordCheck off
.oncheck :- turns BadWordCheck on (if it is off)

Moderators and admins are given a secret keyword through which they can bypass the 5 minute mute.

.src :- view link for the source code
.help :- Get help



Thank you. If there are any recommendations for features of the bot feel free to share.
```"""
    
    )

    

    

keep_alive()
client.run(#Hidden For Security Purposes)
