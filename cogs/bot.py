import discord
from discord.ext import commands


class BotCog(commands.Cog, name='Bot'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'We have logged in as {self.bot.user}')

    @commands.Cog.listener()
    async def on_message(self, message):
        uname = str(message.author)
        u_msg = message.content
        channel = str(message.channel)
        if message.author == self.bot.user:
            return

        if message.content.lower() == 'ping':
            await message.channel.send('pong')
        
        await self.bot.process_commands(message)


async def setup(bot):
    await bot.add_cog(BotCog(bot))