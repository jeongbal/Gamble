from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context
from discord.message import Message

from utils.money import MoneyExt


class Money(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.money = MoneyExt()

    @commands.command(name="돈", aliases=["지갑", "ㄷ", "ㅈㄱ", "wr", "ehs", "e"])
    async def _money(self, ctx: Context):
        msg: Message = await ctx.send(embed=Embed(title="불러오는 중"))
        embed = await self.money.money(ctx.author.id)
        await msg.edit(embed=embed)

    @commands.command(name="출석", aliases=["ㅊㅅ", "ct", "cnftjr", "cㅅ"])
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def _attend(self, ctx: Context):
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed = await self.money.attend(ctx)
        await msg.edit(embed=embed)

    @commands.command(name="랭킹", aliases=["ㄹㅋ", "fz", "fㅋ"])
    async def _ranking(self, ctx: Context):
        msg: Message = await ctx.send(embed=Embed(title="불러오는 중"))
        embed = await self.money.ranking(ctx)
        await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(Money(bot))
