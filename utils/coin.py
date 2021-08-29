from utils.database.mongo import Mongo
import os
from random import randint
from discord.embeds import Embed
from datetime import datetime, timezone


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
            if random_amount <= -4950:
                random_amount = -50000
            elif random_amount >= 4950:
                random_amount = 50000
            price = coin["price"]
            new_price = (
                price + random_amount
                if price + random_amount > 0
                else price + abs(random_amount)
            )
            await self.mongo.update_coin_price(coin["name"], new_price, price)

    async def coin_list(self, next: datetime) -> Embed:
        coin_list = await self.mongo.get_all_coins_data()
        now = datetime.now(timezone.utc)
        embed = Embed(title="코인 시세")
        for coin in coin_list:
            updown_icon = (
                ":chart_with_upwards_trend:"
                if coin["price"] >= coin["previous"]
                else ":chart_with_downwards_trend:"
            )
            increasing = coin["price"] - coin["previous"]
            sign = "+" if increasing >= 0 else "-"
            embed.add_field(
                name=f"{self.__coin_emoji[coin['name']]} {coin['name']}",
                value=f"{updown_icon} {format(coin['price'], ',')}원 ({sign}{format(abs(increasing))})",
            )
        embed.set_footer(text=f"시세는 5분마다 변경됩니다. | 다음 갱신까지: {(next - now).seconds}초")
        return embed

    async def purchase(self, user_id: int, coin: str, amount: int) -> Embed:
        if not await self.mongo.exchange_coin(user_id, coin, amount):
            return Embed(title="잔고가 부족합니다.")
        user_data = await self.mongo.get_user_data(user_id)
        return Embed(
            title="구매 성공",
            description=f"잔고: {user_data['money']} | {self.__coin_emoji[coin]} 소지량: {user_data['coins'][coin]}",
        )

    async def sell(self, user_id: int, coin: str, amount: int) -> Embed:
        if not await self.mongo.exchange_coin(user_id, coin, -amount):
            return Embed(title="코인이 부족합니다.")
        user_data = await self.mongo.get_user_data(user_id)
        return Embed(
            title="판매 성공",
            description=f"잔고: {user_data['money']} | {self.__coin_emoji[coin]} 소지량: {user_data['coins'][coin]}",
        )

    async def user_coin(self, user_id: int) -> Embed:
        user_data = await self.mongo.get_user_data(user_id)
        user_coins = user_data["coins"]
        embed = Embed(title="코인 지갑")
        for coin, amount in user_coins.items():
            embed.add_field(name=f"{self.__coin_emoji[coin]}", value=f"{amount}개")
        return embed

    async def full_purchase(self, user_id: int, coin: str) -> Embed:
        user_data = await self.mongo.get_user_data(user_id)
        user_money = user_data["money"]
        coin_data = await self.mongo.get_coin_price(coin)
        amount = user_money // coin_data["price"]
        if amount == 0:
            return Embed(title="돈이 부족합니다.")
        await self.mongo.exchange_coin(user_id, coin, amount)
        new_user_data = await self.mongo.get_user_data(user_id)
        return Embed(
            title="구매 성공",
            description=f"잔고: {new_user_data['money']} | {self.__coin_emoji[coin]} 소지량: {new_user_data['coins'][coin]}",
        )

    async def full_sell(self, user_id: int, coin: str) -> Embed:
        user_data = await self.mongo.get_user_data(user_id)
        user_coins = user_data["coins"]
        if user_coins[coin] == 0:
            return Embed(title="코인이 부족합니다.")
        await self.mongo.exchange_coin(user_id, coin, -user_coins[coin])
        new_user_data = await self.mongo.get_user_data(user_id)
        return Embed(
            title="구매 성공",
            description=f"잔고: {new_user_data['money']} | {self.__coin_emoji[coin]} 소지량: {new_user_data['coins'][coin]}",
        )
