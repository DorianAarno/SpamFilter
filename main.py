from discord import *
from discord.ext import commands
import os, traceback

bot = commands.Bot(case_insensitive=True, command_prefix='.')

@bot.event
async def on_ready():
    print('*********\nBot is Ready.\n*********')

@bot.event
async def on_message(ctx):
    if ctx.channel.id == 854560382009737228:
        return
    from SpamFilter.antispam import AntiSpam
    if ctx.author.bot:
        return
    try:
        test = await AntiSpam(dictionary=True).check(bot, ctx.channel, ctx.author)
        if test:
            await ctx.channel.send("SPAM")
        print(test)
    except:
        print(traceback.format_exc())



# for file in os.listdir('./cogs'):
#     if file.endswith('.py') and file != '__init__.py':
#         try:
#             bot.load_extension("cogs."+file[:-3])
#             print(f"{file[:-3]} Loaded successfully.")
#         except:
#             print(f"Unable to load {file[:-3]}.")
#             print(traceback.format_exc())

bot.run("ODYwNDAxMDg2Mjc1MTI1MjQ4.YN6s9A.AdE_JdH9G_D_NGiTK-W0C7ZEehw")
