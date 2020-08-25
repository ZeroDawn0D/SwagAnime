import discord;
from discord.ext import commands;
import os;
import main as sc;

RIRIKSU = os.environ.get("RIRIKSU");
client = discord.Client();

@client.event
async def on_ready():
	print("Bot is ready.");

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	helpSearch = ">help ";
	animeSearch = ">anime ";
	songSearch = ">song ";
	if message.content.startswith(animeSearch):
		input = message.content[len(animeSearch):];
		animeNameLink = sc.pageSearch(input);
		messageToSend = "";
		c = 1;
		for i in animeNameLink:
			messageToSend = messageToSend + str(c) + ": "+ i[0] + "\n";
			c+=1;
		
		await message.channel.send(messageToSend);

client.run(RIRIKSU);
