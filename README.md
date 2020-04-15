# Telegram-Wilson
[![Build Status](https://drone.quving.com/api/badges/Quving/telegrambot-wilson/status.svg)](https://drone.quving.com/Quving/telegrambot-wilson)

## Description
Telegram-Wilson is a [telegrambot](https://core.telegram.org/bots/api), with which you can chat in a natural way. This chatbot is powered by [cleverbot](https://www.cleverbot.com/), a well-known chatbot that learns to imitate human conversations by communicating with people.
In this open source repository you can find the source code and instructions how to host this telegrambot on your own.
___
#### Click [here](https://t.me/cleverwilson_bot) to chat with Wilson.
___
## Configuration
In the configuration file 'phrases.json' you can define how your botinstance should respond.

```json
{
  "INTRODUCTION": "Hi, I'm Wilson. Usually I'm only avail...",
  "GREETING": "Yep?",
  "GOODBYE": "Too bad ... see you next time.",
  "HELP": "If you write with me and I don't answer, then ..."
}
```

## Installation
Before you can host this instance on your own, you must officially register your bot with Telegrambot. You can find the instructions [here](https://core.telegram.org/bots) (3. How do i create a bot?)

After you had the conversation with Botfather, you received a bot_token. This bot_token is relevant for the setup.

### Docker (recommended)
#### Build and use your own Docker-Image
```bash
docker build -t telegrambot-wilson .
docker run -d -v $(pwd)/phrases.json:/app/phrases.json \
    -e BOT_TOKEN=<your-bot-token> \
    --name telegrambot-wilson telegrambot-wilson
```

## Usage
Once your bot is running you can interact with it. You can find the bot at Telegram under '@[bot_username]'. Note: bot_username ends with 'bot'. You start the conversation session with the initial command:
```
Hey Wilson
```

The bot-instance will reply when it is launched succesfully. Happy chatting!
