from telegram.ext import Updater,MessageHandler,Filters,CallbackContext
from telegram import Update

import os
TOKEN = os.environ['TOKEN']

updater = Updater(TOKEN)

#Handler
def echo(update: Update, context: CallbackContext):
    pass

updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))
