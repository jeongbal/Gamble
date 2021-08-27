import discord
from discord.ext import commands

from utils.admin import AdminExt


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.admin = AdminExt()

    @commands.command(name="set_money")
    @commands.is_owner()
    async def _set_money(self, ctx, user_id: int, money: int):
        msg = await ctx.send(embed=discord.Embed(title="ㄱㄷ"))
        embed = await self.admin.set_money(user_id, money)
        await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))
