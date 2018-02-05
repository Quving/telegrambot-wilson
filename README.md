[![Build Status](http://drone.quving.com/api/badges/Quving/telegrambot-wilson/status.svg)](http://drone.quving.com/Quving/telegrambot-wilson)
## Telegrambot-Wilson
This repository provides [dockerized](https://www.docker.com/what-docker) scripts to launch and host your own chatter-[telegrambot](https://telegram.org/). 

![alt text](https://chatterbot.readthedocs.io/en/stable/_images/banner.png)


## Concept of Wilson
This Telegrambot creates a client with the famous chatter bot [cleverbot](http://www.cleverbot.com/) using a virtualframe buffered browser. Messages to the bot will be forwarded to the cleverbot client. The responses will be parsed and returned to the telegrambot. Simple, isn't it? 

### Installation:
``` docker build -t telegrambot-wilson .```

### Launch:
Once you have had the conversation with [botfather](https://telegram.me/BotFather) and received your own bot-token, you can host your bot instance by yourself with the folling command:
``` docker run -d -e BOT_TOKEN=$(BOT_TOKEN) --name  telegrambot-wilson telegrambot-wilson```
