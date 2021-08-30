"""
discord.py help command generator

https://github.com/Saebasol/Hiyobot_deprecated/blob/v4/hiyobot/cogs/general/help.py

BSD 3-Clause License

Copyright (c) 2020, Ryu JuHeon
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""


import discord
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context
from discord.embeds import Embed
from discord.message import Message


class General(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.command(name="초대")
    async def _invite(self, ctx: Context):
        """
        이 봇의 초대 링크를 보여줍니다.
        사용 예시: ``;초대``
        """
        url = discord.utils.oauth_url(self.bot.user.id)
        await ctx.send(url)

    @commands.command(name="help", aliases=["도움말", "도움", "ㅗ디ㅔ"])
    async def _help(self, ctx: Context):
        msg: Message = await ctx.send(embed=Embed(title="ㄱㄷ"))
        embed = Embed(title="명령어 목록")
        command_list = [
            command
            for command in self.bot.commands
            if command.name not in ["jishaku", "set_money", "help"]
        ]
        for command in command_list:
            embed.add_field(name=command.name, value=command.help)
        await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
