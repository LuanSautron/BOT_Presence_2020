import discord 
import sqlite3

client = discord.Client()
db = sqlite3.connect("profiles.db")
cursor = db.cursor()

async def check_mail_epitech(message, mail):
    suffix = ""
    try:
        suffix = mail.split('@')[1]
    except IndexError:
        await message.author.send("There is a problem with your mail !")
        return 0
    if suffix == "epitech.eu":
        return 1
    await message.author.send("There is a problem with your mail !")
    return 0


async def register_student(message, db):
    try:
        mail = message.content.split(' ')[1]
        c = await check_mail_epitech(message, mail)
        if c == 0:
            return
    except IndexError:
        return
    id = message.author.id
    try:
        db.execute("INSERT INTO profiles(profile_id, email) VALUES (?, ?)", (id, mail))
    except sqlite3.IntegrityError:
        print("This ID already register with this mail : " + mail)
        await message.author.send("You already register with this mail " + mail + ". If it's not your mail, please contact an AER or an Admin")
        return
    db.commit();
    await message.author.send("You succefully register !")
    print("New student: " + mail)


async def check_presence(message, db):
    id = message.author.id

    try:
        cursor.execute("SELECT email FROM profiles WHERE profile_id=?", (str(id), ))
        mail = cursor.fetchone()
        if mail == None:
            await message.author.send("Hmm... You aren't register try this command first : /register [email]")
            print("Not register : " + str(id))
            return
    except:
        return
    print("Student is: " + mail[0])
    await message.author.send("All is good, because you're here !")

tab = [["register", register_student], ["present", check_presence]]

@client.event
async def on_ready():
    print("Logged on as [{}]".format(client.user))

@client.event
async def on_message(message):
    if message.content[0] != '/':
        return;
    try:
        command = message.content.split('/')[1].split(' ')[0]
    except:
        return
    for i in tab:
        if command == i[0]:
            await i[1](message, db)

client.run("token")
db.close();