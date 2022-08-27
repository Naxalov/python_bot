from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

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
    inlineKeyboard = InlineKeyboardButton('INLINE',callback_data='data 123')

    reply_markup = InlineKeyboardMarkup([[inlineKeyboard]])
    update.message.reply_text(txt,reply_markup=reply_markup)
    return 

def getQuery(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer('DONE',show_alert=True)
    print(query.data)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))
updater.dispatcher.add_handler(CallbackQueryHandler(getQuery))
updater.start_polling()
updater.idle()