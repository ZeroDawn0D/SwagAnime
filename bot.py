import discord
from discord.ext import commands

client = discord.Client();

@client.event
async def on_ready():
	print("Bot is ready.");

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('.uwu '):
		messageToSend = message.content[5:];
		await message.channel.send(messageToSend);	

client.run("NzQzODk3Mjg0ODM1NjcyMTM2.XzbWVQ.RAmfl88LpTWFhO36quIIPwLqkOM");
