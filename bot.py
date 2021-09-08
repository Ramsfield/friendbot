import discord
import discord.utils
import os
import json

from random import seed
from random import randint
from random import choice
from discord.ext import commands

# Bot Setup -- Attempt to set up greeting. If it fails, then go without it
intents = discord.Intents(messages=True, guilds=True)
try:
    intents.members = True
    bot = commands.Bot(command_prefix='$', intents=intents)
except:
    bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(pass_context=True)
async def screenshot(ctx, arg1=None):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if arg1 is None:
        # Generate 2 alpha
        arg1 = ''.join([choice(alpha) for _ in range(2)])
        arg1 += ''.join([str(randint(0,9)) for _ in range(4)])
    await ctx.send("https://prnt.sc/" + arg1)


@bot.command(pass_context=True)
async def cc(ctx, *, arg=None):
    role = ctx.author.roles[1]

    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    await role.edit(color=discord.Color.from_rgb(red, green, blue))

@bot.command(pass_context=True)
async def nickme(ctx):
    member = ctx.author
    names = None
    with open("names.json") as f:
        names = json.load(f)

    name = choice(names)
    try:
        await member.edit(nick=name)
    except:
        await ctx.send("Unable to change your nickname, sorries")

bot.run(os.getenv('TOKEN'))
