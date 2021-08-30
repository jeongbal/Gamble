from utils.database.mongo import Mongo
from discord.embeds import Embed
from discord.ext import commands, tasks
from discord.ext.commands.context import Context
from discord.message import Message
from utils.coin import CoinExt


class Coin(commands.Cog):
    def __init__(self, bot: commands.Bot, mongo: Mongo) -> None:
        self.bot = bot
        self.coin = CoinExt(mongo)
        self.update_price.start()

    @tasks.loop(seconds=180)
    async def update_price(self) -> None:
        await self.coin.update_price()

    @commands.command(name="코인", aliases=["zd", "ㅋㅇ", "zㅇ"])
    async def _coin(self, ctx: Context):
        """
        코인 시세를 보여줍니다.
        사용 예시: ``;코인``
        """
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        next = self.update_price.next_iteration
        embed = await self.coin.coin_list(next)
        await msg.edit(embed=embed)

    @commands.command(name="구매", aliases=["ra", "ㄱㅁ", "rㅁ"])
    async def _purchase(self, ctx: Context, coin: str, amount: int):
        """
        코인을 구매합니다.
        사용 예시: ``;구매 btc 3``
        """
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed = await self.coin.purchase(ctx.author.id, coin, amount)
        await msg.edit(embed=embed)

    @commands.command(name="판매", aliases=["va", "ㅍㅁ", "vㅁ"])
    async def _sell(self, ctx: Context, coin: str, amount: int):
        """
        코인을 판매합니다.
        사용 예시: ``;판매 btc 3``
        """
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed = await self.coin.sell(ctx.author.id, coin, amount)
        await msg.edit(embed=embed)

    @commands.command(name="코인지갑", aliases=["ㅋㅇㅈㄱ", "zdwr"])
    async def _coin_wallet(self, ctx: Context):
        """
        현재 소지중인 코인들을 보여줍니다.
        사용 예시: ``;코인지갑``
        """
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed = await self.coin.user_coin(ctx.author.id)
        await msg.edit(embed=embed)

    @commands.command(name="풀매수", aliases=["ㅍㅁㅅ", "vat"])
    async def _full_purchase(self, ctx: Context, coin: str):
        """
        코인을 최대치로 구매합니다.
        사용 예시: ``;풀매수 btc``
        """
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed = await self.coin.full_purchase(ctx.author.id, coin)
        await msg.edit(embed=embed)

    @commands.command(name="풀매도", aliases=["ㅍㅁㄷ", "vae"])
    async def _full_sell(self, ctx: Context, coin: str):
        """
        코인을 전부 판매합니다.
        사용 예시: ``;풀매도 btc``
        """
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed = await self.coin.full_sell(ctx.author.id, coin)
        await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(Coin(bot, bot.mongo))
