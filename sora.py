import discord
import random
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
      print("봇 연결 성공 !")
      #await bot.change_presence(activity=discord.Game(name="지웅이가 만듬 ㅎㅎ"))

@bot.event
async def on_message(message):
      if message.content.endswith("?"):
            a = random.randrange(0, 5)

            if a==1:
                  a = "안 돼."
            elif a==2:
                  a = "그럼."
            elif a==3:
                  a = "가만히 있어."
            elif a==4:
                  a = "다시 한번 물어봐."

            await message.channel.send(a)
      else:
            message.channel.send("물음표 붙여.")
      

bot.run(os.environ['token'])