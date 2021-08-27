from discord.ext.commands import Cog
from discord.ext.commands.errors import CommandOnCooldown


class Error(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandOnCooldown):
            await ctx.send(
                f"해당 명령어는 아직 사용할 수 없습니다.\n{round(error.retry_after)}초 후에 다시 시도하세요."
            )
        raise error


def setup(bot):
    bot.add_cog(Error(bot))
