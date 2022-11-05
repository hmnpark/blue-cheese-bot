import discord
from discord.ext import commands
import datetime
import asyncio


PRIVILEGED_IDS = {135960976863264770}
COGS = [
    'owner',
    'bot',
    'menu'
]


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True
    bot = commands.Bot(command_prefix='?', intents=intents, owner_id = 135960976863264770)

    for cog in COGS:
        asyncio.run(bot.load_extension(f'cogs.{cog}'))

    with open('token.txt') as fp:
        TOKEN = fp.read()
    bot.run(TOKEN)
