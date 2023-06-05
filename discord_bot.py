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

        # Replace phrases like "should we", "could we", "could I" from the sentence
        sentence = sentence.replace("should we", "").replace("could we", "").replace("could i", "").strip()

        # Splitting the sentence based on ' or '
        parts = sentence.split(' or ')

        choice1 = parts[0].strip("should I").strip("should we").strip("could we").strip("could I").strip("?") if len(
            parts) > 0 else None
        choice2 = parts[1].strip("should I").strip("should we").strip("could we").strip("could I").strip("?") if len(
            parts) > 1 else None

        if choice1 and choice2:
            decision = choice([choice1, choice2])

            # Strip characters from the decision based on the sentence
            decision = decision.strip("?").strip()

            with open('log.txt', 'a') as f:
                f.write(f'{message.author.name} requested: {message.content}\n')
            await message.channel.send(decision)
        else:
            with open('log.txt', 'a') as f:
                f.write(f'{message.author.name} requested an invalid choice: {message.content}\n')
            await message.channel.send("Please provide at least two choices separated by 'or'.")


if __name__ == "__main__":
    client.run('DISCORD API') 
