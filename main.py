import discord
from discord.ext import tasks, commands
import asyncio

from discord.ext.commands.core import _CaseInsensitiveDict

intents = discord.Intents.default( )
intents.members = True

TOKEN = 'ODc2ODQ0ODU1NjY4NjU0MTky.YRp_aA.8WgmI7bjf4IoCgn24K_o3mRH9AU'
bot = commands.Bot(command_prefix='--', _CaseInsensitive=True, intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')

@bot.command(pass_context=True)
async def t_com(ctx):
    await ctx.send('Test command, ignore.') 

bot.run(TOKEN)