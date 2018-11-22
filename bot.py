import discord
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config['SECRETS']['client_id']

client = discord.Client()

commands = {
    "!help": "displays available commands",
    "!register": "add yourself as a user",
    "!addclass": "add a class to your schedule",
    "!addevent": "add an event to your schedule",
    "!free": "displays who's free at the current time"
}

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        command = message.content.split()[0][1:]
        if command == 'help':
            await respond(message.channel, "__**Available Commands**__:\n%s" % (''.join(['**%s**: %s\n' % (k, v) for k, v in commands.items()])))
        elif command == 'register':
            pass
        elif command == 'addclass':
            pass
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