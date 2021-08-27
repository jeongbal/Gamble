from typing import Optional, cast
from motor.motor_asyncio import AsyncIOMotorClient


class Mongo:
    def __init__(self, mongo_db_url: str) -> None:
        self.__client = AsyncIOMotorClient(mongo_db_url)
        self.__user_data = self.__client.gamble.user_data

    async def initialize_user(self, user_id: int, user_name: str) -> None:
        await self.__user_data.insert_one(
            {"user_id": user_id, "money": 0, "name": user_name}
        )

    async def get_user_data(self, user_id: int) -> Optional[dict[str, int]]:
        return await self.__user_data.find_one({"user_id": user_id})

    async def set_user_money(self, user_id: int, money: int) -> None:
        await self.__user_data.update_one(
            {"user_id": user_id}, {"$set": {"money": money}}
        )

    async def get_all_users_data(self, limit: int) -> None:
        return cast(
            list[dict[str, any]],
            await self.__user_data.find({})
            .sort("money", -1)
            .limit(limit)
            .to_list(limit),
        )
