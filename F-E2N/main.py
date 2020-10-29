import discord 
from student import Student, DBCo
from event import Event
import sqlite3

client = discord.Client()

@client.event
async def on_ready():
    print("Logged on as [{}]".format(client.user))

@client.event
async def on_message(message):
    e = Event(message)
    msg = e.do()
    if msg != None:
        await message.author.send(msg)

client.run("Njk3NTExMDQzNTEyOTI2MzE5.Xo4Vxw.UQzrhEenj-GWhybVc_gcw5AuS9Y")
DBCo().close()