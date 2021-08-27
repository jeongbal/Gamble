from discord import Embed
from utils.database.mongo import Mongo
import os


class AdminExt:
    def __init__(self) -> None:
        self.mongo = Mongo(os.getenv("MONGO_DB_URL"))

    async def set_money(self, user_id, money) -> Embed:
        await self.mongo.set_user_money(user_id, money)
        return Embed(
            title="잔고 수정", description=f"<@{user_id}>: {money}", color=0x00FF00
        )
