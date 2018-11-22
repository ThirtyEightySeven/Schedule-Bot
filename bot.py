from model.data import Data
import discord
import configparser
from model.course import Course
from model.event import Event

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
        split_message = message.content.split()
        command = split_message[0][1:]
        args = None        
        if len(split_message) > 1:
            args = split_message[1:]
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
            if len(args) == 3:
                if message.author.id in data.db['users'] and args[1] not in data.db['users'][message.author.id].schedule.courses:
                    data.db['users'][message.author.id].schedule.add_course(Course(args[0], args[1], args[2]))
                    # data.write_data()
                    await respond(message.channel, "Added successfully.")                
                else:
                    await respond(message.channel, "You're not registered.")
            else:
                 await respond(message.channel, "Usage: !addcourse <id> <time> <place>\nExample: !addcourse CSCI140 MWF12P2P GOL")

        elif command == 'addevent':
            if message.author.id in data.db['users']:
                data.db['users'][message.author.id].schedule.add_event(Event(args[0], args[1]))
                # data.write_data()
            else:
                await respond(message.channel, "You're not registered.")
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