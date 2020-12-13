#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time

import telegram
from telegram import ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from chatbotinstance import ChatbotInstance
from config import Config


def start(update, context):
    update.message.reply_text(INTRODUCTION)


def reset_chatbot_instance(update, context):
    if str(update.message.chat_id) in sessions.keys():
        update.message.reply_text("(Wilson dieded)")
        sessions[str(update.message.chat_id)].reset()
        update.message.reply_text("(Wilson respawned")
        update.message.reply_text("... warum?")


def kill_chatbot_instance(update, context):
    sessions[str(update.message.chat_id)].kill()
    sessions.pop(str(update.message.chat_id))
    update.message.reply_text(GOODBYE)


def start_chatbot(update, context):
    new_user = {str(update.message.chat_id): ChatbotInstance()}
    sessions.update(new_user)
    update.message.reply_text(GREETING)
    Config.logger.info("New user ({}) start interacting with the bot.".format(update.message.chat_id))


def chat(update, context):
    chat_id = str(update.message.chat_id)
    chatsession = sessions.get(chat_id, None)
    if chatsession and chatsession.is_ready():
        reply = sessions[chat_id].chat(update.message.text)
        context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        time.sleep(random.randint(0, 3))
        update.message.reply_text(reply)


def help(update, context):
    update.message.reply_text(HELP)


def error(update, context):
    """Log Errors caused by Updates."""
    Config.logger.warning('Update "%s" caused error "%s"', update, context.error)


def parse_message(update, context):
    dictionary_switch = {
        update.message.text.lower(): chat,
        "hey wilson": start_chatbot,
        "bye wilson": kill_chatbot_instance,
        "stirb wilson": reset_chatbot_instance
    }

    dictionary_switch[update.message.text.lower()](update, context)


if __name__ == '__main__':
    sessions = {}

    # Phrases
    HELP = Config.PHRASES['HELP']
    GOODBYE = Config.PHRASES['GOODBYE']
    GREETING = Config.PHRASES['GREETING']
    INTRODUCTION = Config.PHRASES['INTRODUCTION']

    updater = Updater(token=Config.BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Create Handlers.
    help_handler = CommandHandler("help", help)
    start_handler = CommandHandler("start", start)
    reset_handler = CommandHandler("reset", reset_chatbot_instance)
    msg_handler = MessageHandler(Filters.text, parse_message)

    # "Add Listeners"
    dispatcher.add_error_handler(error)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(reset_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(msg_handler)

    # Start polling
    updater.start_polling()
    updater.idle()
