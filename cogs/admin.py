import discord
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.message import Message

from utils.admin import AdminExt


class Admin(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.admin = AdminExt()

    @commands.command(name="set_money")
    @commands.is_owner()
    async def _set_money(self, ctx, user_id: int, money: int):
        msg: Message = await ctx.send(embed=discord.Embed(title="ㄱㄷ"))
        embed: Embed = await self.admin.set_money(user_id, money)
        await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))
