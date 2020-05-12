import os
import random
import discord  
from discord.ext import commands

token = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    """ 起動時実行 """
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def team(ctx, num=2):
    """ 単純なチーム分け """
    member_list = [member.name for member in ctx.author.voice.channel.members]
    random.shuffle(member_list)
    msg = list()
    for i in range(num):
        team_member = ', '.join(member_list[i:len(member_list):num])
        msg.append(''.join(['> team', str(i+1), ' : ', team_member]))
    await ctx.channel.send('\n'.join(msg))

bot.run(token)