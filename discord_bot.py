import os
import discord
from dotenv import load_dotenv
import random

load_dotenv()

client = discord.Client(intents=discord.Intents.all())

def decide(options):
    return random.choice(options)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.decide'):
        options = message.content.split(' ')[1:]
        decision = decide(options)
        await message.channel.send(decision)

if __name__ == "__main__":
    client.run(os.getenv("DISCORD_TOKEN"))
