import discord
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config['SECRETS']['client_id']

client = discord.Client()


@client.event
async def on_message(message):
    pass


@client.event
async def respond(channel, msg):
    await client.send_message(channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    # await client.change_presence(game=discord.Game(name="on Michael's MacBook."))

client.run(TOKEN)