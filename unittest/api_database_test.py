import unittest
from src.database import api
import threading
import discord
from discord.ext import commands
from src.models.bot import Yadis
from src.models import discord as DiscordModels
from src.database import api
import asyncio

class TestDatabase(unittest.TestCase):
    def setUp(self) -> None:
        open("src\\database\\test.db", "w").close()

        self.bot = Yadis(
            token="MTExODgyNjAzMjAyODQ2MzE0Ng.GSDF2H.epnRn6061g0L1-J7PQzvQ9p37m8DIqNYQ5S3jM",
            owner_ids=[529302484901036043],
            debug_channel_id=1120278847888314389,  # type: ignore
            intents=0,  # type: ignore
        )
        
        t = threading.Thread(target=self.bot.run, daemon=True)
        t.start()
    
    def test_add_get_guild(self):
        while not self.bot.is_ready():
            pass
        
        tmp_channel = self.bot.guilds[0].get_channel(1120273667734126614)
        guild = DiscordModels.Guild(self.bot.guilds[0], tmp_channel)
        asyncio.run(api.add_guild(guild))
        guild2 = asyncio.run(api.get_guild(self.bot, guild=guild))


if __name__ == "__main__":
    unittest.main()
