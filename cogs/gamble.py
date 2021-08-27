from discord.embeds import Embed
from discord.ext import commands

from utils.gamble import GambleExt


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gamble = GambleExt()

    @commands.command(name="돈", aliases=["지갑", "ㄷ", "ㅈㄱ", "wr", "ehs", "e"])
    async def _money(self, ctx):
        msg = await ctx.send(embed=Embed(title="불러오는 중"))
        embed = await self.gamble.money(ctx.author.id)
        await msg.edit(embed=embed)

    @commands.command(name="출석", aliases=["ㅊㅅ", "ct", "cnftjr"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def _attend(self, ctx):
        msg = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed = await self.gamble.attend(ctx.author.id)
        await msg.edit(embed=embed)

    @commands.command(name="랭킹", aliases=["ㄹㅋ"])
    async def _ranking(self, ctx):
        msg = await ctx.send(embed=Embed(title="불러온느 중"))
        embed = await self.gamble.ranking()
        await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(Gamble(bot))
