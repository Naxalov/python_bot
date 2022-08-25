import telegram
import os
TOKEN=os.environ['TOKEN']
bot = telegram.Bot(token=TOKEN)
user = bot.getMe()
print(type(user))
print(user.id)
print(user.first_name)
print(bot.getMe())