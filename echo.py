from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler
from telegram import Update

import os
TOKEN = os.environ['TOKEN']

updater = Updater(TOKEN)

#Handler
def echo(update: Update, context: CallbackContext):
    txt=update.message.text
    user_id = update.message.from_user.id
    bot = context.bot
    bot.sendMessage(user_id,txt)
    return 

def start(update: Update, context: CallbackContext):
    txt='Welcome to our echo bot'
    user_id = update.message.from_user.id
    bot = context.bot
    bot.sendMessage(user_id,txt)
    return 


updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()