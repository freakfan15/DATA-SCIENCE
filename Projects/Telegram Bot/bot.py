import logging
from os import startfile
from telegram.ext import Updater
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "1732575384:AAG9sAGIQXUUJvP9FPV1V_8bzAFVwR-VMF4"

def start(bot, update):
    print(update)
    author = update.message.from_user.first_name
    msg = update.message.text
    reply = "Hi! {}".format(author)
    bot.send_message(chat_id = update.message.chat_id, text = reply)

def help(bot, update):
    help_txt = "Hey! I am FreakBot. Here to help you {}".format(update.message.from_user.first_name)
    bot.send_message(chat_id = update.message.chat_id, text = help_txt)

def echo_text(bot,update):
    reply = update.message.text
    bot.send_message(chat_id = update.message.chat_id, text = reply)

# def echo_sticker(bot, update):
#     bot.send_sticker(chat_id=update.message.chat_id, sticker = update.message.file_id)

def error(bot, update):
    logger.error("Update '%s' caused error '%s' ", update, update.error)


def main():
    updater = Updater(TOKEN) # it will recieve updates from telegram server

    dp = updater.dispatcher # handler of the received updates
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo_text))
    # dp.add_handler(CommandHandler(Filters.sticker, echo_sticker))
    dp.add_error_handler(error)

    updater.start_polling()
    logger.info("Started Polling")
    updater.idle()

if __name__=="__main__":
    main()