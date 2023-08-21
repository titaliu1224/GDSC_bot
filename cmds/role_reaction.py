import discord
from discord.ext import commands
from discord.ext.commands.core import command
from core.classes import Cog_Extension

class Reaction(Cog_Extension):
    
    # 認領身分組
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        emo = str(data.emoji) # 用戶選擇的emoji
        guild = self.bot.get_guild(834741375299485726)
        
        # 限定特定訊息
        if data.message_id == 1008675994854490152 :
            if emo == '😀':
                role = guild.get_role(1007957947768385546)  # 社群居民
                await data.member.add_roles(role)
                user = guild.get_member(data.user_id)
                
                role = guild.get_role(878671045110947911) # 請去認領身分組
                await user.remove_roles(role)
        
        elif data.message_id == 1008677150007763016 :
            if emo == '🥸':
                role = guild.get_role(1007958540998168576) # 社群長老
                await data.member.add_roles(role)

    # 當取消表情符號時
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, data):
        emo = str(data.emoji)
        guild = self.bot.get_guild(834741375299485726)
        
        # 限定特定訊息
        if data.message_id == 1008675994854490152 :
            if emo == '😀':
                user = guild.get_member(data.user_id)
                role = guild.get_role(1007957947768385546)  # 社群居民
                await user.remove_roles(role)

                role = guild.get_role(878671045110947911) # 請去認領身分組
                await data.member.add_roles(role)

        elif data.message_id == 1008677150007763016 :
            if emo == '🥸':
                user = guild.get_member(data.user_id)
                role = guild.get_role(1007958540998168576) # 社群長老
                await user.remove_roles(role)
        
            
async def setup(bot):
    await bot.add_cog(Reaction(bot))