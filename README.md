cat > README.md <<EOF
# Discord Decision Bot

This is a Discord bot written in Python using the \`discord\` library. The bot can help you make decisions by providing random choices from given options.

## Prerequisites

Before running the bot, make sure you have the following prerequisites installed:
- Python 3.x
- \`discord\` library (\`pip install discord.py\`)
- \`dotenv\` library (\`pip install python-dotenv\`)

## Getting Started

To get started with the bot, follow these steps:
1. Clone the repository or download the code:
   \`git clone <repository_url>\`

2. Create a new file named \`.env\` and open it in a text editor:
   \`touch .env && code .env\`

3. In the \`.env\` file, add the following line and replace \`DISCORD_API_TOKEN\` with your Discord API token:
   \`DISCORD_API=DISCORD_API_TOKEN\`

4. Save and close the \`.env\` file.

5. Run the bot:
   \`python bot.py\`

## Usage

To ask the bot to make a decision, use the \`.decide\` command followed by your question:
\`.decide Should I go for a walk today?\`

The bot will randomly respond with either 'Yes' or 'No'.

To ask the bot to make a choice between multiple options, use the \`.choice\` command followed by your options separated by 'or':
\`.choice Pizza or Burger or Sushi?\`

The bot will randomly select and respond with one of the given options.

## Logging

The bot logs the requests made by users in the \`log.txt\` file.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request. Any contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code according to your needs.
EOF
