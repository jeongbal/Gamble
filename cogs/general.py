import discord
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="초대")
    async def _invite(self, ctx):
        await ctx.send(
            "https://discord.com/oauth2/authorize?client_id=880483042190323722&scope=bot&permissions=2146954615"
        )


def setup(bot):
    bot.add_cog(General(bot))
