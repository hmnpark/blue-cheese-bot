import discord
from discord.ext import commands
from Menu.Menu import Menu
from datetime import date


EXCLUSIONS = {'The Farm Stand/ Salad Bar', 'Ember/Grill', "Farmer's Market", 'Sizzle Grill'}
COLORS = {
    'Breakfast': 0xffe100,
    'Lunch': 0xff9800,
    'Dinner': 0x651ce3
}
REFRESH_TIME = 8


def _make_embed(menu, period, date, exclusions):
    embed = discord.Embed(title=f'{menu.get("name")}',
                            description=f'{period} {date}',
                            color=COLORS[period])
    for k in menu.get(period):
        if k not in exclusions:
            embed.add_field(
                name=k,
                value=''.join([f'> • {food}\n' for food in menu.get(period).get(k)]),
                inline=True)
    return embed


class MenuCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.menu = Menu()
    
    def _menu_check(self):
        if self.menu.today != date.today().strftime('%m/%d/%Y') and date.now().hour >= REFRESH_TIME:
            self.menu.force_update_menu()

    @commands.command(name='breakfast')
    async def _breakfast(self, ctx, *args):
        self._menu_check()
        if len(args) > 0 and args[0] == 'all':
            exclusions = set()
        else:
            exclusions = EXCLUSIONS

        embed = _make_embed(self.menu.brandywine, 'Breakfast', self.menu.today, exclusions)
        await ctx.send(embed=embed)
        embed = _make_embed(self.menu.anteatery, 'Breakfast', self.menu.today, exclusions)
        await ctx.send(embed=embed)

    @commands.command(name='lunch')
    async def _lunch(self, ctx, *args):
        self._menu_check()
        if len(args) > 0 and args[0] == 'all':
            exclusions = set()
        else:
            exclusions = EXCLUSIONS

        embed = _make_embed(self.menu.brandywine, 'Lunch', self.menu.today, exclusions)
        await ctx.send(embed=embed)
        embed = _make_embed(self.menu.anteatery, 'Lunch', self.menu.today, exclusions)
        await ctx.send(embed=embed)

    @commands.command(name='dinner')
    async def _dinner(self, ctx, *args):
        self._menu_check()
        if len(args) > 0 and args[0] == 'all':
            exclusions = set()
        else:
            exclusions = EXCLUSIONS

        embed = _make_embed(self.menu.brandywine, 'Dinner', self.menu.today, exclusions)
        await ctx.send(embed=embed)
        embed = _make_embed(self.menu.anteatery, 'Dinner', self.menu.today, exclusions)
        await ctx.send(embed=embed)

    @commands.command(name='refresh')
    @commands.is_owner()
    async def _refresh(self, ctx):
        self.menu.force_update_menu()
        await ctx.send('Refreshed menu!')


async def setup(bot):
    await bot.add_cog(MenuCog(bot))
