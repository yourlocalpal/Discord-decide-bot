#Discord Decision Bot

This is a simple Python script that uses the discord library and Flask framework to create a decision-making bot for Discord. The bot listens for messages in a Discord channel that contain the .decide command and responds with a randomly generated "Yes" or "No" answer.

Requirements

    Python 3.5 or later
    discord library
    Flask framework

Usage

    Install the discord and Flask libraries by running pip install discord flask in the command line.
    Replace the REPLACE WITH YOUR API placeholder in client.run() with your Discord bot API token.
    Run the script using python discord_bot.py in the command line.
    Invite the bot to your Discord server and grant it appropriate permissions.
    Use the .decide command followed by a question to request a "Yes" or "No" answer from the bot.

Note: The bot logs all requests and responses to a file named log.txt, which can be accessed by visiting the Flask server running on localhost:5000.

License

This script is licensed under the GNU General Public License v3.0 License. See the LICENSE file for more information.

You don't need flask to be up for this to work, I am adding it for log keeping. Who requests the bot and passes it to a webui.
