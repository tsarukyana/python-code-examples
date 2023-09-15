from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
import openai

# Your Telegram bot token from BotFather
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
# Your OpenAI API key
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'

openai.api_key = OPENAI_API_KEY


def start(update: Update, context: None):
    """
    This function is the entry point for starting the conversation with the bot.
    It takes two parameters, `update` and `context`.
    The `update` parameter represents the incoming message update, and the `context` parameter is not used in this function.

    Parameters:
        update (Update): The incoming message update.
        context (None): Not used in this function.

    Returns:
        None
    """
    update.message.reply_text("Hello! Ask me anything, and I'll reply using OpenAI.")


def ask_openai(update: Update, context: None):
    """
        Generate a response to a given question using the OpenAI API.

        Args:
            update (Update): The incoming message update.
            context (None): The context object, not used in this function.

        Returns:
            None: This function does not return anything.
    """
    question = update.message.text
    response = openai.Completion.create(engine="davinci", prompt=question, max_tokens=150)
    update.message.reply_text(response.choices[0].text.strip())


def main():
    """
    Runs the main function of the program.
    Initializes the Updater object with the provided token and sets it to use context.
    Initializes the Dispatcher object.
    Adds a CommandHandler to the Dispatcher for the "start" command, which calls the start function.
    Adds a MessageHandler to the Dispatcher for text messages that are not commands,
    which calls the ask_openai function.
    Starts polling for updates from the Telegram API.
    Keeps the program running until it is interrupted.
    """
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, ask_openai))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
