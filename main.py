import discord
# from Menu.Menu import Menu
# from discord.ext import tasks
from discord.ext import commands
# from commands.menu import EmbedCog
import datetime
import asyncio

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents, owner_id = 135960976863264770)

PRIVILEGED_IDS = {135960976863264770}
COGS = [
    'owner',
    'menu'
]


# def _build_menu(menu, period):
#     msg = f'{period}\n__{menu.get("name")}__\n'
#     for k,v in menu.get(period).items():
#         if k == 'The Farm Stand/ Salad Bar' or k == "Farmer's Market":
#             continue
#         msg += f'***{k}***\n'
#         for item in v:
#             msg += '\t' + item + '\n'
#         msg += '\n'
#     msg += '\n'
#     return msg


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    uname = str(message.author)
    u_msg = message.content
    channel = str(message.channel)
    #print(f'{uname} said: "{u_msg}" ({channel})')
    if message.author == bot.user:
         return

    if message.content.lower() == 'ping':
        await message.channel.send('pong')
    
    await bot.process_commands(message)


with open('token.txt') as fp:
    TOKEN = fp.read()


# def initial_load_cogs(bot):
#     for cog in COGS:
#         asyncio.run(bot.load_extension(f'cogs.{cog}'))


# async def start_bot(bot):
#     initial_load_cogs(bot)
#     bot.run(TOKEN)


if __name__ == '__main__':
    for cog in COGS:
        asyncio.run(bot.load_extension(f'cogs.{cog}'))
    bot.run(TOKEN)
