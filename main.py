#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from chatbot import Chatbot
from config import Config

updater = Updater(token=Config.BOT_TOKEN)
dispatcher = updater.dispatcher

sessions = {}

# Phrases
HELP = Config.PHRASES['HELP']
GOODBYE = Config.PHRASES['GOODBYE']
GREETING = Config.PHRASES['GREETING']
INTRODUCTION = Config.PHRASES['INTRODUCTION']


def start(bot, update):
    bot.sendMessage(update.message.chat_id, INTRODUCTION)


def reset_chatbot_instance(bot, update):
    if str(update.message.chat_id) in sessions.keys():
        bot.sendMessage(update.message.chat_id, "(Wilson dieded)")
        sessions[str(update.message.chat_id)].resetChatbot()
        bot.sendMessage(update.message.chat_id, "(Wilson respawned")
        bot.sendMessage(update.message.chat_id, "... warum?")


def kill_chatbot_instance(bot, update):
    sessions[str(update.message.chat_id)].killChatbot()
    sessions.pop(str(update.message.chat_id))
    bot.sendMessage(update.message.chat_id, GOODBYE)


def start_chatbot(bot, update):
    newUser = {str(update.message.chat_id): Chatbot()}
    sessions.update(newUser)
    bot.sendMessage(update.message.chat_id, GREETING)


def chat(bot, update):
    if (str(update.message.chat_id) in sessions.keys() and
            sessions[str(update.message.chat_id)].isOn()):
        reply = sessions[
            str(update.message.chat_id)].talk(update.message.text)
        bot.sendMessage(update.message.chat_id, reply)


def help(bot, update):
    bot.sendMessage(update.message.chat_id, HELP)


def parse_message(bot, update):
    dictionary_switch = {
        update.message.text.lower(): chat,
        "hey wilson": start_chatbot,
        "bye wilson": kill_chatbot_instance,
        "stirb wilson": reset_chatbot_instance
    }

    dictionary_switch[update.message.text.lower()](bot, update)


# Create Handlers.
help_handler = CommandHandler("help", help)
start_handler = CommandHandler("start", start)
reset_handler = CommandHandler("reset", reset_chatbot_instance)
msg_handler = MessageHandler([Filters.text], parse_message)

# "Add Listeners"
dispatcher.add_handler(help_handler)
dispatcher.add_handler(reset_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(msg_handler)

# Start polling
updater.start_polling()
