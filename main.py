from disnake import *
from disnake.ext import commands
import os, traceback

bot = commands.Bot(case_insensitive=True, command_prefix='.', intents=Intents.default())

@bot.event
async def on_ready():
    print('*********\nBot is Ready.\n*********')

bot.remove_command('help')

@bot.command()
async def ping(ctx):
    await ctx.send (f"📶 {round(bot.latency * 1000)}ms")

# @bot.event
# async def on_command_error(ctx,error):
#     if isinstance(error, (commands.CommandNotFound)):
#         return

@bot.event
async def on_message(ctx):
    if ctx.channel.id == 854560382009737228:
        return
    from SpamFilter.antispam import AntiSpam
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
