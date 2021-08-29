from utils.database.mongo import Mongo
import os
from typing import Any
from random import randint
from discord.embeds import Embed


class CoinExt:
    def __init__(self) -> None:
        self.mongo = Mongo(os.getenv("MONGO_DB_URL"))
        self.__coin_emoji = {
            "btc": "<:btc:881234727821008966>",
            "doge": "<:doge:881233749872869478>",
            "eth": "<:eth:881234867797524480>",
            "xlm": "<:xlm:881233920295841843>",
            "xrp": "<:xrp:881234544357937152>",
        }

    async def update_price(self) -> None:
        coin_list = await self.mongo.get_all_coins_data()
        for coin in coin_list:
            random_amount = round(randint(-5000000, 5000000) / 1000)
            price = coin["price"]
            new_price = (
                price + random_amount
                if price + random_amount > 0
                else price + abs(random_amount)
            )
            await self.mongo.update_coin_price(coin["name"], new_price, price)

    async def coin_list(self) -> Embed:
        coin_list = await self.mongo.get_all_coins_data()
        embed = Embed(title="코인 시세")
        for coin in coin_list:
            updown_icon = (
                ":chart_with_upwards_trend:"
                if coin["price"] >= coin["previous"]
                else ":chart_with_downwards_trend:"
            )
            embed.add_field(
                name=f"{self.__coin_emoji[coin['name']]} {coin['name']}",
                value=f"{updown_icon} {format(coin['price'], ',')}원",
            )
        embed.set_footer(text="시세는 5분마다 변경됩니다.")
        return embed
