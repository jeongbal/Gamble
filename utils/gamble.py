from discord import Embed
from utils.database.mongo import Mongo
import os
from random import randint


class GambleExt:
    def __init__(self) -> None:
        self.mongo = Mongo(os.getenv("MONGO_DB_URL"))

    async def money(self, user_id: int) -> Embed:
        if user_data := await self.mongo.get_user_data(user_id):
            return Embed(
                title="잔고",
                description=f"**{format(user_data['money'], ',')}**원",
                color=0x30807C,
            )
        await self.mongo.initialize_user(user_id)
        return Embed(title="지갑 없음", description="지갑을 생성합니다.", color=0x80307C)

    async def attend(self, user_id: int) -> Embed:
        if user_data := await self.mongo.get_user_data(user_id):
            current = user_data["money"]
            amount = randint(10000, 100000) // 1000 * 1000
            await self.mongo.set_user_money(user_id, current + amount)
            return Embed(title=f"출석하여 {amount}원을 받았습니다.")
        return Embed(title="지갑이 없습니다.", description="`.돈` 명령어로 지갑을 생성하세요.")

    async def ranking(self, ctx) -> Embed:
        ranking = await self.mongo.get_all_users_data(10)
        embed = Embed(title="Top 10")
        for user in ranking:
            embed.add_field(
                name=f"{await ctx.bot.fetch_user(user['user_id'])}",
                value=f"{format(user['money'], ',')}원",
                inline=False,
            )
        return embed
