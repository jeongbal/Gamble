from discord.activity import Game
from discord.enums import Status
from discord.ext import commands
from pathlib import Path
import os
from utils.database.mongo import Mongo


bot = commands.Bot(command_prefix=";", help_command=None)
bot.mongo = Mongo(os.getenv("MONGO_DB_URL"))
token = os.environ["DISCORD_TOKEN"]

cwd = Path(__file__).parents[0]
cwd = str(cwd)
bot.cwd = cwd


@bot.event
async def on_ready():
    print("Bot is ready")
    await bot.change_presence(status=Status.online, activity=Game(";help"))


if __name__ == "__main__":
    for file in os.listdir(os.path.join(cwd, "cogs")):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.{file[:-3]}")
    bot.load_extension("jishaku")
    bot.run(token)
