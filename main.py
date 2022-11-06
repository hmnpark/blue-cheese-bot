import discord
from discord.ext import commands
import asyncio
from Menu.Menu import Menu


PRIVILEGED_IDS = {135960976863264770}
OWNER_ID = 135960976863264770
INITIAL_COGS = [
    'owner',
    'bot',
    'menu'
]


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True
    bot = commands.Bot(
        command_prefix='?',
        intents=intents,
        owner_id=OWNER_ID
        )

    bot.menu = Menu() 

    for cog in INITIAL_COGS:
        asyncio.run(bot.load_extension(f'cogs.{cog}'))

    with open('token.txt') as fp:
        TOKEN = fp.read()
    bot.run(TOKEN)
