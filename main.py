#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chatbot import Chatbot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s' +
                    '- %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

# Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN")


updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher

chatbothandler = {}


def start(bot, update):
    bot.sendMessage(update.message.chat_id, "Ein Wilson, zwei Wilsies!")


def resetWilson(bot, update):
    if str(update.message.chat_id) in chatbothandler.keys():
        bot.sendMessage(update.message.chat_id, "(Wilson dieded)")
        chatbothandler[str(update.message.chat_id)].resetChatbot()
        bot.sendMessage(update.message.chat_id, "(Wilson respawned")
        bot.sendMessage(update.message.chat_id, "... warum?")


def killWilson(bot, update):
    chatbothandler[str(update.message.chat_id)].killChatbot()
    chatbothandler.pop(str(update.message.chat_id))
    bot.sendMessage(update.message.chat_id, "...")


def startWilson(bot, update):
    newUser = {str(update.message.chat_id): Chatbot()}
    chatbothandler.update(newUser)
    bot.sendMessage(update.message.chat_id, "yup?")


def chat(bot, update):
    if (str(update.message.chat_id) in chatbothandler.keys() and
            chatbothandler[str(update.message.chat_id)].isOn()):
        reply = chatbothandler[
            str(update.message.chat_id)].talk(update.message.text)
        bot.sendMessage(update.message.chat_id, reply)


def userhelp(bot, update):
    bot.sendMessage(update.message.chat_id, "Rufe mich mit 'Hey Wilson'. " +
                    "Dann antworte ich auch auf deine Nachrichten. " +
                    "Mit 'Bye Wilson' bin ich wieder afk :D")


def msgParser(bot, update):
    dictionary_switch = {
        update.message.text.lower(): chat,
        "hey wilson": startWilson,
        "bye wilson": killWilson,
        "stirb wilson": resetWilson
    }[update.message.text.lower()](bot, update)


# Create Handlers.
help_handler = CommandHandler("help", userhelp)
start_handler = CommandHandler("start", start)
reset_handler = CommandHandler("resetWilson", resetWilson)
msg_handler = MessageHandler([Filters.text], msgParser)


# "Add Listeners"
dispatcher.add_handler(help_handler)
dispatcher.add_handler(reset_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(msg_handler)


# Start polling
updater.start_polling()
