from utils.database.mongo import Mongo
import os
from random import randint
from discord.embeds import Embed


class GambleExt:
    def __init__(self) -> None:
        self.mongo = Mongo(os.getenv("MONGO_DB_URL"))

    async def probability_gamble(self, user_id: int, bet: int, leverage: int) -> Embed:
        user_data = await self.mongo.get_user_data(user_id)
        user_money = user_data["money"]
        if user_money < bet:
            return Embed(title="돈이 부족합니다.")
        result = randint(0, round(leverage / 0.7))
