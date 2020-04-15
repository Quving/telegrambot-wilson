# Telegram-Wilson
[![Build Status](https://drone.quving.com/api/badges/Quving/telegram-wilson/status.svg)](https://drone.quving.com/Quving/telegram-wilson)

## Description
Telegram-Wilson is a [telegrambot](https://core.telegram.org/bots/api), with which you can chat in a natural way. This chatbot is powered by [cleverbot](https://www.cleverbot.com/), a well-known chatbot that learns to imitate human conversations by communicating with people.

In this open source repository you can find the source code and instructions how to host this telegrambot on your own.

## Concept of Wilson
This Telegrambot creates a client with the famous chatter bot [cleverbot](http://www.cleverbot.com/) using a virtualframe buffered browser. Messages to the bot will be forwarded to the cleverbot client. The responses will be parsed and returned to the telegrambot. Simple, isn't it?

## Installation
Before you can host this instance on your own, you must officially register your bot with Telegrambot. You can find the instructions [here](https://core.telegram.org/bots) (3. How do i create a bot?)

After you had the conversation with Botfather, you received a bot_token. This bot_token is relevant for the setup.

### Docker (recommended)
#### Build and use your own Docker-Image
```bash
docker build -t telegram-wilson .
docker run -d -e BOT_TOKEN=$(BOT_TOKEN) --name telegram-wilson telegrambot-wilson
```

## Usage
Once your bot is running you can interact with it. You can find the bot at Telegram under '@[bot_username]'. Note: bot_username ends with 'bot'. You start the conversation session with the initial command:
```
Hey Wilson
```

The bot-instance will reply when it is launched succesfully. Happy chatting!
