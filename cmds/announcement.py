import discord
from discord.ext import commands, tasks
from discord.ext.commands.core import command
from core.classes import Cog_Extension
import json, datetime, asyncio

#  讀取設定檔
with open("setting.json", 'r', encoding = "utf8") as jfile:
    jdata = json.load(jfile)


class Announcement(Cog_Extension):
    
    def __init__(self, *args, **kwargs):
        # 跑父類別的__init__
        super().__init__(*args, **kwargs)
    
        # 開始循環執行發布公告
        self.announce.start()

    # 循環執行發布公告
    @tasks.loop(hours = 48.0)
    async def announce(self):
        # 測試1: 867032295750893578，bot公告: 877534432578392094
        self.channel = self.bot.get_channel(877534432578392094)

        print(f"Announcement sent! '{jdata['AnnounceContent'][AnnNum]}'")
        AnnNum = int(jdata['AnnounceNum'])

        await self.channel.send(f"{jdata['AnnounceContent'][AnnNum]}")

    

    def setAnnouncementNum(self, timeSet, announceNum):
        with open("setting.json", 'w', encoding = "utf8") as f:
            jdata['AnnounceNum'] = announceNum
            json.dump(jdata, f, indent = 4)
        
    
        
    # @commands.command()
    # async def isclose(self, ctx):
    #     print(self.bot.is_closed())


async def setup(bot):
    await bot.add_cog(Announcement(bot))