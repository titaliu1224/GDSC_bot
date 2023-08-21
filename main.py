import json
import os  # os.listdir
import asyncio

import discord
from discord.ext import commands

import keep_alive

#  讀取設定檔
with open("setting.json", 'r', encoding="utf8") as jfile:
	jdata = json.load(jfile)

intents = discord.Intents.all()
intents.members = True  # 開啟要訂閱的功能(event裡的那種)

bot = commands.Bot(command_prefix=".", intents=intents,
                    help_command=None)  # bot的instance，prefix是指令前綴


@bot.event
async def on_ready():  # 當bot上線了
	print(">>>> Bot is Online <<<<")

@bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
	if extension == "?":
		await print_extensions(ctx)

	await bot.load_extension(f"cmds.{extension}")
	await ctx.send(f"{extension} loaded!")


@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
	if extension == "?":
		await print_extensions(ctx)

	await bot.unload_extension(f"cmds.{extension}")
	await ctx.send(f"{extension} unloaded!")


@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
	if extension == "?":
		await print_extensions(ctx)

	await bot.reload_extension(f"cmds.{extension}")
	await ctx.send(f"{extension} reloaded!")

async def print_extensions(ctx):
	files = ''
	for filename in os.listdir("./cmds"):
		if filename.endswith(".py"):
			files += f"{filename[:-3]}\n"

	await ctx.send(f"現有 extensions: ```\n{files}```")

async def main():
	# load cmds資料夾裡所有.py檔
	for filename in os.listdir("./cmds"):
		if filename.endswith(".py"):
			await bot.load_extension(f"cmds.{filename[:-3]}")
			print(f"{filename} is loaded!")

	token = "YOUR TOKEN HERE"
	await bot.start(token)
    
if __name__ == "__main__":
    # keep_alive.keep_alive()
	asyncio.run(main())

