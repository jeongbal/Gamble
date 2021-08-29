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

    @tasks.loop(seconds=300)
    async def update_price(self) -> None:
        await self.coin.update_price()

    @commands.command(name="코인", aliases=["zd", "ㅋㅇ", "zㅇ"])
    async def _coin(self, ctx):
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed: Embed = await self.coin.coin_list()
        await msg.edit(embed=embed)

    @commands.command(name="구매", aliases=["ra", "ㄱㅁ", "rㅁ"])
    async def _purchase(self, ctx: Context, coin: str, amount: int):
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed: Embed = await self.coin.purchase(ctx.author.id, coin, amount)
        await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(Coin(bot))
