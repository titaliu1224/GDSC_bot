import asyncio
import json
import os
import random

import discord
from discord.ext import commands

from core.classes import Cog_Extension

#  讀取設定檔
with open("setting.json", 'r', encoding = "utf8") as jfile:
    jdata = json.load(jfile)

message_content = ['', '', '', '', ''] #存近5次發送的訊息

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member): # 有成員加入伺服器
        print(f"{member} join!")

        # id = str( member )[-4:]
        # db[id] = 0

        welcome_channel = self.bot.get_channel(self.WelcomeChannel)
        role_channel = self.bot.get_channel(self.RoleChannel)

        await welcome_channel.send(f"歡迎{member.mention}來到元智GDSC！請前往{role_channel.mention}選擇相應身分組，希望你玩得開心！") 
        # 異步執行要用await呼叫，去官方API看誰是異步誰不是。send是在頻道中傳訊息

        # 給請領取身份組身份組
        guild = self.bot.get_guild(834741375299485726)
        role = guild.get_role(878671045110947911)  #指定身分組
        await member.add_roles(role)

    '''
    # 有成員離開伺服器
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} leave qwq")

        welcome_channel = self.bot.get_channel(self.WelcomeChannel)
        
        # channel = self.bot.get_channel(int(welcome_channel))
        await welcome_channel.send(f"{str(member)[:-5]} 走了qwq") 
        # 異步執行要用await呼叫，去官方API看誰是異步誰不是。send是在頻道中傳訊息
    '''
    
    # 偵測傳出來的每一則訊息
    @commands.Cog.listener()
    async def on_message(self, msg):

        #-----------------特殊關鍵字區-----------------#
        if(msg.author.id != 869558965267234907):
            if msg.content.startswith("早安") or msg.content.endswith("早安"):
                await msg.channel.send("安呀")

            if msg.content.startswith("午安") or msg.content.endswith("午安"):
                await msg.channel.send("安呀")

            if msg.content.startswith("晚安") or msg.content.endswith("晚安"):
                await msg.channel.send("ZZZZ")
                
            if msg.content.startswith("<@869558965267234907>") or msg.content.endswith("<@!869558965267234907>"):
                await msg.channel.send("?")
                
            if msg.content.startswith("兔子") or msg.content.endswith("兔子"):
                await msg.channel.send("兔子可愛")
            
            print(msg.content)

        #-----------------避免洗版區-------------------#
        if msg.author.id != 869558965267234907 and msg.author.id != 235088799074484224 and msg.content != '': 
            await self.noisy(msg)
            

    async def noisy(self, msg):
        del message_content[0]
        message_content.append(msg.content)
        stop = True;

        for i in range(1, 5):
            if message_content[i - 1] != message_content[i]:
                stop = False

        if stop:
            await msg.channel.send("洗版bad:confused: 你被禁言10分鐘了")
            print(f"{msg.author}在洗版，洗版內容:")    
            print(message_content) 

            # 刪除社群身份組
            guild = msg.guild
            grade1 = guild.get_role(1007957947768385546)
            grade2 = guild.get_role(1007958540998168576)

            role_record = 0

            authorRole = msg.author.roles

            if grade1 in authorRole:
                role_record = 1
                await msg.author.remove_roles(grade1)
            if grade2 in authorRole:
                role_record = 2
                await msg.author.remove_roles(grade2)


            # 給予閉嘴身分組
            noisy_role = guild.get_role(922183963311734814)
            await msg.author.add_roles(noisy_role)
            await asyncio.sleep(600)
            await msg.author.remove_roles(noisy_role)

            # 將年級身分組加回來
            if role_record == 1:
                await msg.author.add_roles(grade1)
            if role_record == 2:
                await msg.author.add_roles(grade2)


async def setup(bot):
    await bot.add_cog(Event(bot))