import discord
import random
from flask import Flask, render_template

client = discord.Client(intents=discord.Intents.all())
app = Flask(__name__)

@app.route('/')
def home():
    with open('log.txt', 'r') as f:
        log = f.readlines()
    return render_template('index.html', log=log)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '.decide' in message.content:
        with open('log.txt', 'a') as f:
            f.write(f'{message.author.name} requested: {message.content}\n')
        question = message.content.lower().replace('.decide', '').strip()
        rand = random.random() # generate a random float between 0 and 1
        if rand < 0.5:
            response = 'Yes'
        else:
            response = 'No'
        await message.channel.send(response)

client.run('REPALCE WITH YOUR API')
