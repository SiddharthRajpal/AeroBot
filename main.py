import discord
import asyncio
from keep_alive import keep_alive
from replit import db
import urllib
import json
from googleapiclient.discovery import build



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

  if message.author in mutelist and msg.startswith("0xFF2021"):
    mutelist.remove(message.author)
    await message.channel.send(f"{message.author} has been unmuted for saying the secret word!!")
    #From Line no 19-38 is BadWordCheck
  if msg.startswith(".subs"):
    api_key = "AIzaSyB3HHetCUqkUQlusSgZgzl_o5oE_uIh8uU"
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
    api_key = "AIzaSyB3HHetCUqkUQlusSgZgzl_o5oE_uIh8uU"
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
    await message.channel.send("Total number of videos uploaded by Aeroblaze Yt:-")
    await message.channel.send("```"+u["videoCount"]+"```")

  if msg.startswith(".src"):
    await message.channel.send("Source code available on github :- https://github.com/SiddharthRajpal/AeroBot")
    


    

keep_alive()
client.run("ODQ0NjMzNzgxOTIzMDg2MzY2.YKVQgg.7gmfPpmH0wWhKl5m54aMbLlo0xs")
