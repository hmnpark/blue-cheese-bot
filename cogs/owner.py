import discord
from discord.ext import commands


class OwnerCog(commands.Cog, name='Owner'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True, name='shutdown')
    @commands.is_owner()
    async def _shutdown(self, ctx):
        await ctx.send('sayonara')
        await ctx.bot.close()


    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, module : str):
        """Loads a module."""
        try:
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send('\N{PISTOL}')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\N{OK HAND SIGN}')


    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, module : str):
        """Unloads a module."""
        try:
            self.bot.unload_extension(module)
        except Exception as e:
            await ctx.send('\N{PISTOL}')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\N{OK HAND SIGN}')


    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def _reload(self, ctx, *, module : str):
        """Reloads a module."""
        try:
            await self.bot.unload_extension(module)
            await self.bot.load_extension(module)
        except Exception as e:
            await ctx.send('\N{PISTOL}')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\N{OK HAND SIGN}')


async def setup(bot):
    await bot.add_cog(OwnerCog(bot))