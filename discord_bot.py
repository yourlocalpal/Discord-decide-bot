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

        # Strip "should I" from the sentence
        sentence = sentence.replace("should i", "").strip()

        # Splitting the sentence based on ' or '
        parts = sentence.split(' or ')

        # Extracting choices
        choice1 = parts[0].strip() if len(parts) > 0 else None
        choice2 = parts[1].strip() if len(parts) > 1 else None

        if choice1 and choice2:
            if "should I" in parts[0]:
                choice1 = choice1.replace("should I", "").strip()
            if "should I" in parts[1]:
                choice2 = choice2.replace("should I", "").strip()

            decision = choice([choice1, choice2])

            # Strip question mark '?' from the decision
            decision = decision.rstrip('?')

            with open('log.txt', 'a') as f:
                f.write(f'{message.author.name} requested: {message.content}\n')
            await message.channel.send(decision)
        else:
            with open('log.txt', 'a') as f:
                f.write(f'{message.author.name} requested an invalid choice: {message.content}\n')
            await message.channel.send("Please provide at least two choices separated by 'or'.")


if __name__ == "__main__":
    client.run('DISCORD API')