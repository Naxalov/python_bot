from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton

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
    key1 = KeyboardButton(text='KeyButton',request_contact=True)
    reply_markup = ReplyKeyboardMarkup([[key1,key1]],input_field_placeholder='Placeholder')
    update.message.reply_text(txt,reply_markup=reply_markup)
    return 


updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()