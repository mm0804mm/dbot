import discord
from discord.ext import commands
import os
client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    await client.change_presence(activity=discord.Game(name="제3의 상현"))
    print("봇 이름:",client.user.name,"봇 아이디",client.user.id,"봇 버전:",discord.__version__)

client.run(os.environ['token'])