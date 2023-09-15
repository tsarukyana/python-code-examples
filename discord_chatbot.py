import discord
import openai

# Initialize discord client
client = discord.Client()

# Your Discord bot token
DISCORD_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
# Your OpenAI API key
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'

openai.api_key = OPENAI_API_KEY

@client.event
async def on_ready():
    """
    Event handler that is called when the client is ready to start receiving events.
    This function does not take any parameters.
    This function does not return any value.
    """
    print(f'Logged in as {client.user.name} ({client.user.id})')

@client.event
async def on_message(message):
    """
    A function that handles the `on_message` event.

    Parameters:
        - message (discord.Message): The message object that triggered the event.
    Returns:
        None
    """
    if message.author == client.user:
        return

    # If message starts with "!ask", the bot will interact with OpenAI API
    if message.content.startswith('!ask'):
        question = message.content[len('!ask '):]  # extract the question
        response = openai.Completion.create(
            engine="davinci",
            prompt=question,
            max_tokens=150
        )
        await message.channel.send(response.choices[0].text.strip())

client.run(DISCORD_TOKEN)
