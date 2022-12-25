import os
import telebot


# Initialize bot
bot = telebot.TeleBot(
    os.environ['BOT_TOKEN'], parse_mode='HTML'
)
