import os

import discord
from discord.ext import commands


class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        
        self.bot = bot

        self.WelcomeChannel = int(834767865264865291)
        self.RuleChannel = int(834767428458250251)
        self.RoleChannel = int(834766967725621258)
        self.BotChannel = int(834803077131010078)

        self.scheduleText = ''
        self.scheduleTime = ''