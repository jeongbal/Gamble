from typing import Any, Optional, cast
from motor.motor_asyncio import AsyncIOMotorClient


class Mongo:
    def __init__(self, mongo_db_url: str) -> None:
        self.__client = AsyncIOMotorClient(mongo_db_url)
        self.__user_data = self.__client.gamble.user_data
        self.__coin_price = self.__client.coin.coin_price

    async def initialize_user(self, user_id: int) -> None:
        await self.__user_data.insert_one({"user_id": user_id, "money": 0})

    async def get_user_data(self, user_id: int) -> Optional[dict[str, int]]:
        return await self.__user_data.find_one({"user_id": user_id})

    async def set_user_money(self, user_id: int, money: int) -> None:
        await self.__user_data.update_one(
            {"user_id": user_id}, {"$set": {"money": money}}
        )

    async def get_all_users_data(self, limit: int) -> list[dict[str, Any]]:
        return cast(
            list[dict[str, Any]],
            await self.__user_data.find({})
            .sort("money", -1)
            .limit(limit)
            .to_list(limit),
        )

    async def get_all_coins_data(self) -> list[dict[str, Any]]:
        return cast(
            list[dict[str, Any]],
            await self.__coin_price.find({}).sort("name", 1).to_list(5),
        )

    async def update_coin_price(self, coin: str, price: int, previous: int) -> None:
        await self.__coin_price.update_one(
            {"name": coin}, {"$set": {"price": price, "previous": previous}}
        )
