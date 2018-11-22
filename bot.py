from model.data import Data
import discord
import configparser
from model.course import Course

data = Data()

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config['SECRETS']['client_id']

client = discord.Client()

commands = {
    "!help": "displays available commands",
    "!info": "displays user information",
    "!register": "add yourself as a user",
    "!unregister": "remove yourself as a user",
    "!addcourse": "add a class to your schedule",
    "!addevent": "add an event to your schedule",
    "!free": "displays who's free at the current time"
}

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        command = message.content.split()[0][1:]
        if len(message.content.split()) > 1:
            args = message.content[1:]
        if command == 'help':
            await respond(message.channel, "__**Available Commands**__:\n%s" % (''.join(['**%s**: %s\n' % (k, v) for k, v in commands.items()])))
        elif command == 'info':
            if message.author.id in data.db['users']:   
                await respond(message.channel, data.db['users'][message.author.id])
            else:
                await respond(message.channel, "You're not registered")
        elif command == 'register':
            if message.author.id not in data.db['users']:
                data.add_user(message.author.id, message.author.name)
                data.write_data()
                await respond(message.channel, "Registration successful.")                
            else:
                await respond(message.channel, "You're already registered.")
        elif command == 'unregister':
            if message.author.id in data.db["users"]:
                data.db['users'].pop(message.author.id)
                data.write_data()
                await respond(message.channel, "Unregistered successfully.")    
            else:
                await respond(message.channel, "You're not registered.")            
        elif command == 'addcourse' and args:
            if message.author.id in data.db['users'] and args[1] not in data.db['users'][message.author.id].schedule.courses:
                data.db['users'][message.author.id].schedule.add_course(Course(args[1], args[2], [3]))
        elif command == 'addevent':
            pass
        elif command == 'free':
            pass
        else:
            await respond(message.channel, "Command wasn't recognized. Use !help to see available commands.")
    

@client.event
async def respond(channel, msg):
    await client.send_message(channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print()

client.run(TOKEN)