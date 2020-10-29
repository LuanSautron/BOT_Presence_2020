import discord 
from student import Student, DBCo
from event import Event
from key import token
import sqlite3
from write import Liststudent, Listpedago

client = discord.Client()
list_s = Liststudent("rh.txt")
list_p = Listpedago("pedago.txt")

@client.event
async def on_ready():
    print("Logged on as [{}]".format(client.user))

@client.event
async def on_message(message):
    e = Event(message)
    msg = e.do(list_s, list_p)
    if msg == "stop":
        await client.close()
    if msg != None:
        await message.author.send(msg)

client.run(token)