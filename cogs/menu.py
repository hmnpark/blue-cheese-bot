import discord
from discord.ext import commands
from Menu.Menu import Menu
import datetime
from datetime import datetime as dt


EXCLUSIONS = {
    'The Farm Stand/ Salad Bar',
    'Ember/Grill',
    "Farmer's Market",
    'Sizzle Grill'
    }
COLORS = {
    'Breakfast': 0xffe100,
    'Lunch': 0xff9800,
    'Dinner': 0x651ce3
    }
REFRESH_HOUR_PST = 8
TIMEZONE = datetime.timezone(-datetime.timedelta(hours=8))


class MenuCog(commands.Cog, name='Menu'):
    bot: commands.Bot

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='breakfast')
    async def _breakfast(self, ctx, *args) -> None:
        """Gets the breakfast menu for today"""
        await self._post_menu(ctx, args, 'Breakfast')

    @commands.command(name='lunch')
    async def _lunch(self, ctx, *args) -> None:
        """Gets the lunch menu for today"""
        await self._post_menu(ctx, args, 'Lunch')

    @commands.command(name='dinner')
    async def _dinner(self, ctx, *args) -> None:
        """Gets the dinner menu for today"""
        await self._post_menu(ctx, args, 'Dinner')

    @commands.command(name='refresh')
    @commands.is_owner()
    async def _refresh(self, ctx) -> None:
        """Refreshes the current menu"""
        self.bot.menu.force_update_menu()
        await ctx.send('Refreshed menu!')

    def _menu_check(self, ctx) -> None:
        """
        Updates the menu if the current date is different,
        and >= the refresh time (hour)
        """
        cur_hour = dt.now().astimezone(tz=TIMEZONE).hour
        cur_day = dt.today().astimezone(tz=TIMEZONE).strftime('%m/%d/%Y')

        if self.bot.menu.today_as_str() != cur_day and cur_hour >= REFRESH_HOUR_PST:
            ctx.send("One second, getting today's menu...")
            self.bot.menu.force_update_menu()

    async def _post_menu(self, ctx, args, period) -> None:
        """Posts the menu"""
        self._menu_check(ctx)
        if len(args) > 0 and args[0] == 'all':
            exclusions = set()
        else:
            exclusions = EXCLUSIONS

        embed = _make_embed(
            self.bot.menu.brandywine,
            period,
            self.bot.menu.today_as_str(),
            exclusions,
            self.bot.menu.time)
        await ctx.send(embed=embed)
        embed = _make_embed(
            self.bot.menu.anteatery,
            period,
            self.bot.menu.today_as_str(),
            exclusions,
            self.bot.menu.time)
        await ctx.send(embed=embed)


def _make_embed(
    menu: dict,
    period: str,
    date: str,
    exclusions: set,
    timestamp: dt
    ) -> discord.Embed:
    """Get the menu as an embed"""
    embed = discord.Embed(title=f'{menu.get("name")}',
                            description=f'{period} {date}',
                            color=COLORS[period])
    embed.timestamp = timestamp
    for k in menu.get(period):
        if k not in exclusions:
            embed.add_field(
                name=k,
                value=''.join(
                    [f'> • {food}\n' for food in menu.get(period).get(k)]
                    ),
                inline=True)
    return embed


async def setup(bot):
    await bot.add_cog(MenuCog(bot))
