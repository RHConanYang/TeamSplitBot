import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='s')

bot.event

async def onready():
    print("bot is online")


bot.event
async def on_member_join(member):
    print(F'{member} join!')


bot.run('ODgzNzgzMjk5NzE2MjM5NDMw.YTO9Vg.YIDbL00i-D-KdLzLHEtvZGVXN2Y')