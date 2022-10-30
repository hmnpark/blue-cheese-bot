import discord
from Menu.menu import Menu
# from discord.ext import tasks
import datetime

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)
MENU = Menu()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    uname = str(message.author)
    u_msg = message.content
    channel = str(message.channel)
    #print(f'{uname} said: "{u_msg}" ({channel})')
    if message.author == client.user:
         return

    if message.content.lower() == 'ping':
        await message.channel.send('pong')
    elif message.content.lower() == '?kill':
        exit()
    elif message.content.lower() == '?refresh':
        MENU.update_menu()
        await message.channel.send('Update completed')
    elif message.content.lower() == '?frefresh':
        MENU.force_update_menu()
        await message.channel.send('Force update completed')
    elif message.content.lower() == '?menu':
        msg = f'{MENU.today}\n__Brandywine__\n'
        for k,v in MENU.brandywine.get('Lunch').items():
            if k == 'The Farm Stand/ Salad Bar' or k == "Farmer's Market":
                continue
            msg += f'***{k}***\n'
            for item in v:
                msg += '\t' + item + '\n'
            msg += '\n'
        msg += '\n'
        await message.channel.send(msg)
        msg = f'__Anteatery__\n'
        for k,v in MENU.anteatery.get('Lunch').items():
            if k == 'The Farm Stand/ Salad Bar' or k == "Farmer's Market":
                continue
            msg += f'***{k}***\n'
            for item in v:
                msg += '\t' + item + '\n'
            msg += '\n'
        await message.channel.send(msg)



# @client.event
# async def end_bot(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('end'):
#         await message.channel.send('byebye')


# @tasks.loop(time=datetime.time(hour=19))
# async def test_task():
#     channel = client.get_channel(1028220387454107658)
#     await channel.send("it's 12pm pst maybe")


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     await message.add_reaction('👎')

# @client.event
# async def on_message2(message):
#     if message.author == client.user:
#         return
#     await message.add_reaction('👍')


with open('token.txt') as fp:
    TOKEN = fp.read()
client.run(TOKEN)
