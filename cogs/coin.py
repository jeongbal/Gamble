from discord.embeds import Embed
from discord.ext import commands, tasks
from discord.ext.commands.context import Context
from discord.message import Message
from utils.coin import CoinExt


class Coin(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.coin = CoinExt()
        self.update_price.start()

    @tasks.loop(seconds=180)
    async def update_price(self) -> None:
        await self.coin.update_price()

    @commands.command(name="코인", aliases=["zd", "ㅋㅇ", "zㅇ"])
    async def _coin(self, ctx: Context):
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed: Embed = await self.coin.coin_list()
        await msg.edit(embed=embed)

    @commands.command(name="구매", aliases=["ra", "ㄱㅁ", "rㅁ"])
    async def _purchase(self, ctx: Context, coin: str, amount: int):
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed: Embed = await self.coin.purchase(ctx.author.id, coin, amount)
        await msg.edit(embed=embed)

    @commands.command(name="판매", aliases=["va", "ㅍㅁ", "vㅁ"])
    async def _sell(self, ctx: Context, coin: str, amount: int):
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed: Embed = await self.coin.sell(ctx.author.id, coin, amount)
        await msg.edit(embed=embed)

    @commands.command(name="코인지갑", aliases=["ㅋㅇㅈㄱ", "zdwr"])
    async def _coin_wallet(self, ctx: Context):
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed: Embed = await self.coin.user_coin(ctx.author.id)
        await msg.edit(embed=embed)

    @commands.command(name="풀매수", aliases=["ㅍㅁㅅ", "vat"])
    async def _full_purchase(self, ctx: Context, coin: str):
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed: Embed = await self.coin.full_purchase(ctx.author.id, coin)
        await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(Coin(bot))
