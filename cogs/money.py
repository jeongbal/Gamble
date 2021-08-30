from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context
from discord.message import Message
from utils.database.mongo import Mongo

from utils.money import MoneyExt


class Money(commands.Cog):
    def __init__(self, bot: Bot, mongo: Mongo):
        self.bot = bot
        self.money = MoneyExt(mongo)

    @commands.command(name="돈", aliases=["지갑", "ㄷ", "ㅈㄱ", "wr", "ehs", "e"])
    async def _money(self, ctx: Context):
        """
        현재 잔고를 보여줍니다. 지갑이 없을 경우 자동으로 생성합니다.
        사용 예시: ``;돈``
        """
        msg: Message = await ctx.send(embed=Embed(title="불러오는 중"))
        embed = await self.money.money(ctx.author.id)
        await msg.edit(embed=embed)

    @commands.command(name="출석", aliases=["ㅊㅅ", "ct", "cnftjr", "cㅅ"])
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def _attend(self, ctx: Context):
        """
        10,000원 ~ 100,000원 을 랜덤으로 지급합니다. 10분마다 사용할 수 있습니다.
        사용 예시: ``;출석``
        """
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed = await self.money.attend(ctx)
        await msg.edit(embed=embed)

    @commands.command(name="랭킹", aliases=["ㄹㅋ", "fz", "fㅋ"])
    async def _ranking(self, ctx: Context):
        """
        유저 랭킹을 소지금 순으로 Top10 까지 표시합니다.
        사용 예시: ``;랭킹``
        """
        msg: Message = await ctx.send(embed=Embed(title="불러오는 중"))
        embed = await self.money.ranking(ctx)
        await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(Money(bot, bot.mongo))
