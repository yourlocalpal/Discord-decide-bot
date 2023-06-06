import os
import discord
from dotenv import load_dotenv
import random

load_dotenv()
client = discord.Client(intents=discord.Intents.all())


def choice(options):
    return random.choice(options)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.decide'):
        with open('log.txt', 'a') as f:
            f.write(f'{message.author.name} requested: {message.content}\n')
        question = message.content.lower().replace('.decide', '').strip()
        rand = random.random()  # generate a random float between 0 and 1
        if rand < 0.5:
            response = 'No'
        else:
            response = 'Yes'
        await message.channel.send(response)

    elif message.content.startswith('.choice'):
        sentence = message.content.lower().replace('.choice', '').strip()
        parts = sentence.split(' or ')

        if len(parts) >= 2:
            choices = []

            for part in parts:
                # Remove phrases like "should I," "should we," "could we," "could I"
                part = part.replace("should we", "").replace("should i", "").replace("could i", "").replace("should they", "").replace("should she", "").strip()
                choices.append(part.rstrip('?'))

            if all(choices):
                decision = choice(choices)

                with open('log.txt', 'a') as f:
                    f.write(f'{message.author.name} requested: {message.content}\n')

                await message.channel.send(decision)
            else:
                await message.channel.send(f"{message.author.name} use choices separated by 'or'")
        else:
            await message.channel.send(f"{message.author.name} use choices separated by 'or'")

if __name__ == "__main__":
    client.run('DISCORD API')

