import discord
from discord.ext import commands
from collections import defaultdict


def _watchlist_alert(menu, watchlist):
    alert = defaultdict(list)
    for station, foods in menu.items():
        for food in foods:
            food = food.lower()
            for item in watchlist:
                item = item.lower()
                if item in food:
                    alert[station].append(food.title())
                    break
    return alert


class NotifyCog(commands.Cog, name='Notify'):
    def __init__(self, bot):
        self.bot = bot
        self.collection = bot.db['users']

    @commands.command(name='notify')
    async def _notify(self, ctx, *args) -> None:
        if not await self._exists_in_watchlist(ctx):
            await ctx.send('Your watchlist is empty! Add to it with `?add thing1 thing2 "thing 3" ...`')
            return

        foods = self.collection.find({"ID": ctx.author.id}, {"foods": 1, "_id": 0})
        foods_list = (await foods.to_list(length=None))[0]['foods']
        b = dict()
        a = dict()
        b['Breakfast'] = _watchlist_alert(self.bot.menu.brandywine['Breakfast'], foods_list)
        b['Lunch'] = _watchlist_alert(self.bot.menu.brandywine['Lunch'], foods_list)
        b['Dinner'] = _watchlist_alert(self.bot.menu.brandywine['Dinner'], foods_list)
        a['Breakfast'] = _watchlist_alert(self.bot.menu.anteatery['Breakfast'], foods_list)
        a['Lunch'] = _watchlist_alert(self.bot.menu.anteatery['Lunch'], foods_list)
        a['Dinner'] = _watchlist_alert(self.bot.menu.anteatery['Dinner'], foods_list)

        msg = '**Brandywine**\n'
        msg += 'Breakfast\n\t' + str(b['Breakfast'])
        msg += '\nLunch\n\t' + str(b['Lunch'])
        msg += '\nDinner\n\t' + str(b['Dinner'])
        msg += '\n\n**Anteatery**'
        msg += '\nBreakfast\n\t' + str(a['Breakfast'])
        msg += '\nLunch\n\t' + str(a['Lunch'])
        msg += '\nDinner\n\t' + str(a['Dinner'])
        await ctx.send(msg)
        
    @commands.command(name='add')
    async def _add(self, ctx, *args) -> None:
        if not args:
            return

        if not await self._exists_in_watchlist(ctx):
            await self.collection.insert_one({"ID": ctx.author.id, "foods": args})

        foods = self.collection.find({"ID": ctx.author.id}, {"foods": 1, "_id": 0})
        foods_list = (await foods.to_list(length=None))[0]['foods']
        foods_union = set(args).union(foods_list)
        sorted_foods = sorted(foods_union)
        await self.collection.update_one({"ID": ctx.author.id}, {"$set": {"foods": sorted_foods}})
        await self._send_watchlist(ctx)

    @commands.command(name='delwatchlist')
    async def _del_watchlist(self, ctx, *args) -> None:
        await self.collection.update_one({"ID": ctx.author.id}, {"$set": {"foods": []}})
        await ctx.send('Deleted your watchlist!')
    
    @commands.command(name='rm')
    async def _rm(self, ctx, *args) -> None:
        if not await self._exists_in_watchlist(ctx):
            await ctx.send('Nothing to remove')
            return
        else:
            num_updated = 0
            for arg in args:
                result = await self.collection.update_one({"ID": ctx.author.id}, {"$pull": {"foods": arg}})
                num_updated += 1 if result.modified_count > 0 else 0
        
        if num_updated == 0:
            await ctx.send('Nothing removed')
        else:
            await self._send_watchlist(ctx)

    @commands.command(name='list')
    async def _list(self, ctx, *args) -> None:
        await self._send_watchlist(ctx)
    
    async def _send_watchlist(self, ctx):
        if not await self._exists_in_watchlist(ctx):
            await ctx.send('Your watchlist is empty! Add to it with `?add thing1 thing2 "thing 3" ...`')
        else:
            foods = self.collection.find({"ID": ctx.author.id}, {"foods": 1, "_id": 0})
            foods_list = (await foods.to_list(length=None))[0]['foods']
            if foods_list:
                await ctx.send(f"Your list: `{', '.join(foods_list)}`")
            else:
                await ctx.send('Your watchlist is empty! Add to it with `?add thing1 thing2 "thing 3" ...`')
    
    async def _exists_in_watchlist(self, ctx):
        count = await self.collection.count_documents({"ID": ctx.author.id})
        if count == 0:
            return False
        else:
            return True


async def setup(bot):
    await bot.add_cog(NotifyCog(bot))