# Spam Filter
A simple and efficient spam filter made to be used in discord bots made with any fork of [discord.py](https://github.com/Rapptz/discord.py)!

# Installation
You can use [pip](https://pip.pypa.io/en/stable/) to install this library.
```
pip install discordpy-antispam
```

# Usage
### Quickstart Guide
```py
from antispam import AntiSpam

@bot.event
async def on_message(msg):
  spam_check = AntiSpam.check(bot, msg.channel, msg.author)
```

### Detailed Guide
```py
from antispam import AntiSpam

dictionary_check = True # Default is False, DO NOT USE THIS IF YOUR SERVER IS MULTI-LINGUAL, Checks if any word in the message is present in english dictionary.
timer_check = True # Default is True, Checks if a member has sent more than 5 messages within 15 seconds, if yes, 6th message is marked as spam.
content_check = True # Default is True, Checks the message's content and if a letter whose occurance in the content is highest covers more than 85% of the content, it marks the message as spam.
history_check = True # Default is True, Checks if the message's content is duplicate of the previous message.

@bot.event
async def on_message(msg):
  spam_check = AntiSpam(
    dictionary = dictionary_check,
    timer = timer_check,
    content = content_check,
    history = history_check
  ).check(bot, msg.channel, msg.author)
```

# Notes
* This library has only been tested with [discord-disnake](https://pypi.org/project/discord-disnake/).
* Your bot needs to have access to message content.

# Contributing
* Fork the repository.
* Add your desired change or filter.
* Open pull request.
* Issues are welcome.
* Consider giving this repository a ⭐, It is highly appreciated!

# License
This repository has been made available via [MIT](https://github.com/DorianAarno/SpamFilter/blob/main/LICENSE) License.
