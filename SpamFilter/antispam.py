import discord
from nltk.corpus import words as dictionary
from datetime import datetime

class AntiSpam():
    def __init__(self, dictionary=False, timer=True, content=True, history=True):
        self._dictionary_check = dictionary
        self._timer_check = timer
        self._content_check = content
        self._history_check = history

    async def check(self,
        bot: discord.Client,
        channel: discord.TextChannel,
        author: discord.Member,
        limit: int = 30
        ):
        # False = Not spamming
        # True = Spam detected
        Messages = []
        async for history in channel.history(limit=limit):
            Messages.append(history)


        if author.id not in [x.author.id for x in Messages]:
            return False

        Author_Messages = []
        for msg in Messages:
            if msg.author.id == author.id:
                Author_Messages.append(msg)

        if self._history_check:
            for i, msg in enumerate(Messages):
                if msg.author.id == author.id:
                    try:
                        if msg.content == Messages[i+1].content:
                            return True
                        else:
                            break
                    except:
                        pass
            
            if len(Author_Messages) >= 2:
                if Author_Messages[0].content == Author_Messages[1].content:
                    return True

        if self._dictionary_check:
            words = Author_Messages[0].content.split(' ')
            for i, word in enumerate(words):
                for letter in word:
                    if not letter.isalpha():
                        words[i] = words[i].replace(letter, '')
            passes = 0
            for word in words:
                if word.lower() in dictionary.words() and len(word) > 1:
                    passes += 1
            if passes < 1:
                return True
        if self._timer_check:
            Time_check_msg = []
            for msg in Author_Messages:
                if (datetime.utcnow() - msg.created_at.replace(tzinfo=None)).seconds < 15:
                    Time_check_msg.append(msg)
            if len(Time_check_msg) >= 5:
                return True

        if self._content_check:
            words = Author_Messages[0].content.split(' ')
            for word in words:
                if len(word) > 35:
                    return True
            words = [x for x in list(Author_Messages[0].content) if x != ' ']
            alpha_dict = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0
            }
            for letter in words:
                for key in alpha_dict.keys():
                    if letter.lower() == key:
                        alpha_dict[key] += 1
            highest_letter_count = 0
            highest_letter = None
            for key in alpha_dict.keys():
                if alpha_dict[key] > highest_letter_count:
                    highest_letter_count = alpha_dict[key]
                    highest_letter = key
            
            if len(words):
                percent = (highest_letter_count/len(words))*100
                if int(round(percent)) > 85:
                    return True

        return False
