import discord
from discord.ext import commands
import asyncio
import motor.motor_asyncio as motor
from Menu.Menu import Menu
import os
from dotenv import load_dotenv
load_dotenv()

OWNER_ID = os.environ['OWNER_ID']
INITIAL_COGS = [
    'owner',
    'bot',
    'menu',
    'notify'
]

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017


def _connect_to_db(bot):
    bot.db = motor.AsyncIOMotorClient(MONGODB_HOST, MONGODB_PORT)['blue_cheese_db']
    

if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True
    bot = commands.Bot(
        command_prefix='?',
        intents=intents,
        owner_id=int(OWNER_ID)
        )

    bot.menu = Menu() 
    _connect_to_db(bot)
    for cog in INITIAL_COGS:
        asyncio.run(bot.load_extension(f'cogs.{cog}'))

    bot.run(os.environ['TOKEN'])
