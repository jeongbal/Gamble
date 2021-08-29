import discord
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="초대")
    async def _invite(self, ctx):
        url = discord.utils.oauth_url(self.bot.user.id)
        await ctx.send(url)


def setup(bot):
    bot.add_cog(General(bot))
