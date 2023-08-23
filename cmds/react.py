import discord
from discord.ext import commands
from discord.ext.commands.core import command
from core.classes import Cog_Extension
import json, random, os, asyncio

# 讀取設定檔
with open("setting.json", 'r', encoding = "utf8") as jfile:
    jdata = json.load(jfile)

    BotChannel = "834803077131010078"

class React(Cog_Extension):

    # 傳送關於社團的所有網址
    @commands.command()
    async def website(self, ctx):
        await ctx.send(
            f'可以在以下網站找到我們:\nFacebook: {jdata["FaceBook"]}\nInstagram: {jdata["Instagram"]}\n自架網站：{jdata["Web"]}\ngoogle官網：{jdata["OfficialWeb"]}')


    # 傳送這個網站(replit)的網址
    @commands.command()
    async def code(self, ctx):
        await ctx.send("我是個開源的bot喔！我的code在這:")
        await ctx.send(jdata['Code'])
    

    # 指令說明
    @commands.command()
    async def help(self, ctx):
        await ctx.send("```\n一般成員可用：\n.help: 呼叫此訊息\n.code: 取得bot的程式碼\n.website: 取得社團所有網站的網址\n.ver: 獲得當前版本資訊\n.ver <不為0之數字>: 獲得完整歷史版本資訊\n```\n```\n管理員專用：\nreload: 上線某個更新過後的檔案\nunload: 下架某個檔案\nload: 上架某個被unloaded的檔案\nload/reload/unload ?: 顯示所有可以 load 的檔案名\ndelete_message <數字>: 刪除<數字>條訊息（beta）```")


    # core team member 資訊
    @commands.command()
    async def core(self, ctx):
        pass

        
    @commands.command()
    async def test(self,ctx):
        print(ctx.author.roles)


    # 印版號&更新記錄
    @commands.command()
    async def ver(self, ctx, history = 0):
        await ctx.channel.send(f"```py\n現在版本：{jdata['Version']}```\n```\n更新日誌：{jdata['VersionNews']}\n```")
        
        # 私訊完整更新記錄
        if history != 0:
            verString = ''
            for ele in jdata['VersionHistory']:
                verString = verString + ele + '\n'

            await ctx.author.send(f"```\n以下是我的完整更新記錄：\n{verString}\n```")

    # 排程發布訊息
    @commands.group()
    async def schedule(self, ctx):
        manual = "- `min + <整數> <文字>`: 在<整數>分鐘後，於當前頻道發送<文字>"
        await ctx.channel.send(f"此為自動排程指令，請使用 `schedule.+以下指令` 完成設定\n其中，`<>`為使用者需輸入的參數\n\n----------------------------------------------\n{manual}\n----------------------------------------------\n")
        await ctx.channel.send("此功能什麼都還沒寫出來，所以不用試了喔ㄎ")        

    # @schedule.command()
    # async def min(self, ctx, minute, text):
    #     with open('scheduleSetting.json', 'rw') as schFile:
    #         schdata = schFile.load()

    #     schdata = 
    #     pass

    @commands.command()
    async def delete_message(self, ctx, limit:int):
        await ctx.channel.purge(limit=limit + 1)
        # await ctx.message.delete()
        message = await ctx.send(f'已刪除 {limit} 則訊息。刪除者：{ctx.author.mention}.')
        await asyncio.sleep(5)
        await message.delete()
            


    """
    # 點數命令群組, 只有管理員可用
    @commands.group()
    async def point(self, ctx):
        pass

    @point.command()
    @commands.has_permissions(administrator = True)
    async def add(self, ctx, id, num):
        if num in db.keys():
            return
        
        point = int( db[id] )
        point += num

        db[id] = str( point )


    @point.command()
    @commands.has_permissions(administrator = True)
    async def take(self, ctx, id, num):
        if num in db.keys():
            return
        
        point = int( db[id] )
        point -= num

        db[id] = point

    # 看自己有多少點數
    @point.command()
    async def see(self, ctx):
        id = ctx.author
        id = str(id)[-4:]

        if(id in db.keys()):
            await ctx.send( f"{ctx.author.mention}，你目前有{db[id]}點，繼續加油！")
        else:
            await ctx.send(f"{ctx.author.mention}，很抱歉，資料庫中沒有你的資訊，請向管理員回報")
            print(f"我在資料庫中沒有找到{ctx.author}的資料")


    # 看別人有多少點數
    @point.command()
    @commands.has_permissions(administrator = True)
    async def check(self, ctx, id):
        id = str(id)

        if(id in db.keys()):
            await ctx.send( f"成員#{id}目前有{db[id]}點")
        else:
            await ctx.send(f"很抱歉，資料庫中沒有#{id}的資訊，他可能尚未發言過")
            print(f"我在資料庫中沒有找到{ctx.author}的資料")

    # 點數規則
    @point.command()
    async def rule(self, ctx):
        await ctx.send(f"點數玩法：\n在{self.bot_channel.mention}和{self.KTV_channel.mention}以外的地方，每說一句話就能獲得一點，獲得的點數可以兌換實體商品。\n關於商品詳情請打指令：.point shop\n:warning: 注意：當你更改了id中的tag或退出群組，點數可能會遺失，如有此情形發生請聯繫bot管理員")
    
    # 點數商店
    @point.command()
    async def shop(self, ctx):
        embed=discord.Embed(title="要兌換商品請向管理員詢問~~", color=0x26ba81)
        embed.set_author(name="點數商店", icon_url="https://openclipart.org/image/400px/213837")
        embed.add_field(name="貼紙套組", value="1000點", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="其他", value="敬請期待", inline=True)
        await ctx.send(embed=embed)
        

    # 取得db的存取連結
    @commands.command()
    async def getdb(self, ctx):
        print(os.getenv("REPLIT_DB_URL"))
        await ctx.send("DB連結已發送在後台，請跟bot管理員索取")
    """


async def setup(bot):
    await bot.add_cog(React(bot))