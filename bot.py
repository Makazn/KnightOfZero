import os
import random
import discord
import code_geass_quotes
import CC
import gifs
import pictures

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Prefix
bot = commands.Bot(command_prefix='z!')


# Watching..
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Code Geass | z!help"))


# z!quote|z!q
@bot.command(name='quote', description='Shows random quotes', aliases=['q'])
async def quote(ctx):
    """Shows you a random quote"""
    response = random.choice(code_geass_quotes.code_geass_quotes)
    await ctx.send(response)


# z!waifu|z!w
@bot.command(name='waifu', description='Shows you best girl', aliases=['w'])
async def waifu(ctx):
    """Shows you best girl"""
    response = random.choice(CC.CC)
    await ctx.send(response)


# z!gif|z!g
@bot.command(name='gif', description='Shows you random gifs', aliases=['g'])
async def gif(ctx):
    """Shows you a random gifs"""
    response = random.choice(gifs.gif)
    await ctx.send(response)


# z!wallpaper|z!wp
@bot.command(name='pic', description='Shows you random pics', aliases=['p'])
async def pic(ctx):
    """Shows you a random picture"""
    response = random.choice(pictures.pic)
    await ctx.send(response)


bot.run("NzM0NDY2MjgzNzg1MTU4NzM2.XxXzoA.S-HGWIj6UfDj4s4TwFuGz37uteE")