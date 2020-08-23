import discord;
from discord.ext import commands;
import os;

RIRIKSU = os.environ.get("RIRIKSU");
client = discord.Client();

@client.event
async def on_ready():
	print("Bot is ready.");

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	animeSearch = ">anime ";
	songSearch = ">song ";

	if message.content.startswith(animeSearch):
		messageToSend = message.content[len(animeSearch):];
		await message.channel.send(messageToSend);	

client.run(RIRIKSU);
