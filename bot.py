from model.data import Data
from model.course import Course
from model.event import Event
from model.event_time import EventTime
import discord
import configparser
import time

data = Data()

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config['SECRETS']['client_id']

client = discord.Client()

commands = {
    "!help": "display available commands",
    "!info": "display user information",
    "!register": "add yourself as a user",
    "!unregister": "remove yourself as a user",
    "!addcourse": "add a course to your schedule",
    "!removecourse": "remove a course from your schedule",
    "!addevent": "add an event to your schedule",
    "!removeevent": "remove an event from your schedule",
    "!free": "display who's free at the current time"
}

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        split_message = message.content.split()
        command = split_message[0][1:]
        args = []
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

        elif command == 'addcourse':
            if len(args) == 3:
                if message.author.id in data.db['users'] and args[1] not in data.db['users'][message.author.id].schedule.courses:
                    course_time = EventTime()
                    course_time.parse_input(args[1])
                    data.db['users'][message.author.id].schedule.add_course(Course(args[0], course_time, args[2]))
                    # data.write_data()
                    await respond(message.channel, "Added successfully.")                
                else:
                    await respond(message.channel, "You're not registered.")
            else: 
                 await respond(message.channel, "Usage: !addcourse <id> <time> <place>\nExample: !addcourse CSCI140 MWF12P2P GOL")

        elif command == 'removecourse':
            if len(args) == 1:
                if args[0] in data.db['users'][message.author.id].schedule.courses:
                    data.db['users'][message.author.id].schedule.courses.pop(args[0])
                    # data.write.data
                    await respond(message.channel, "Course successfully removed.")
                else:
                    await respond(message.channel, "Course is not in your schedule.")
            else:
                await respond(message.channel, "Usage !removecourse <id>")

        elif command == 'addevent':
            if len(args) == 2:
                if message.author.id in data.db['users']:
                    data.db['users'][message.author.id].schedule.add_event(Event(args[0], args[1]))
                    # data.write_data()
                else:
                    await respond(message.channel, "You're not registered.")
            else:
                await respond(message.channel, "Usage: !addevent <name> <time>")   

        elif command == 'removeevent':
            if len(args) == 1:
                if data.db['users'][message.author.id].schedule.events[args[0]] in data.db['users'][message.author.id].schedule.events:
                    data.db['users'][message.author.id].schedule.events.pop(args[0])
                    # dara.write_data
                    await respond(message.channel, "Event successfully removed.")
                else:
                    await respond(message.channel, "Event is not in your schedule.")
            else:
                await respond(message.channel, "Usage: !removeevent <name>")

        elif command == 'free':
            current_time = time.asctime(time.localtime(time.time()))    
            day = current_time[:3]
            time = int(current_time.split()[3].replace(':','')[:4])
            await respond(message.channel, "Day: %s" % (current_time[:3]))

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
