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
        # Extract choices by removing "or" and splitting on ","
        choices = sentence.replace(' or ', ',').split(',')

        # Remove any leading/trailing whitespace from choices
        choices = [choice.strip() for choice in choices]

        # Detecting valid choice question
        if len(choices) > 1:
            decision = choice(choices)
            with open('log.txt', 'a') as f:
                f.write(f'{message.author.name} requested: {message.content}\n')
            await message.channel.send(decision)
        else:
            with open('log.txt', 'a') as f:
                f.write(f'{message.author.name} requested an invalid choice: {message.content}\n')
            await message.channel.send("Please provide multiple choices.")



if __name__ == "__main__":
    client.run('DISCORD API')
