from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Dictionary to store user IDs and their assigned names
user_names = {}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot. Use /addname to associate a name with your user ID.')

def add_name(update: Update, context: CallbackContext) -> None:
    if len(context.args) != 1:
        update.message.reply_text('Usage: /addname <name>')
        return

    user_id = update.message.from_user.id
    name = context.args[0]
    user_names[user_id] = name
    update.message.reply_text(f'Name "{name}" has been associated with your ID!')

def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id in user_names:
        name = user_names[user_id]
        reply_message = f"@{name}, you mentioned something!"
        update.message.reply_text(reply_message)

def main() -> None:
    # Replace 'YOUR_API_TOKEN' with your bot's API token
    updater = Updater("7074174207:AAEq0IE0boTT-nXXQGyLQhM59k8Iude4Fb8", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("addname", add_name))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
