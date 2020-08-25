import discord;
from discord.ext import commands;
import os;
import main as sc;

RIRIKSU = os.environ.get("RIRIKSU");
client = discord.Client();

info = ">info"; i = ">i"; # bot info
search = ">search "; srch = ">srch "; # anime name search IMPLEMENTED
song = ">song ";s = ">s "; # choose song
anime = ">anime ";a = ">a "; # choose anime IMPLEMENTED
currentanime = ">currentanime";ca = ">ca"; #current anime list IMPLEMENTED
currentsong = ">currentsong"; cs = ">cs"; #current song list
getAnime = ">getanime";ga = ">ga"; #get current chosen anime IMPLEMENTED


currentAnimeNameLink = ("","");
currentSongNameLink = ("","");

animeNameLink = list();
songNameLink = list();

def currentAnimeFunction():
	messageToSend = "";
	c = 1;
	for i in animeNameLink:
		messageToSend = messageToSend + str(c) + ": "+ i[0] + "\n";
		c+=1;
	print("\"" + str(animeNameLink) + "\"");
	return messageToSend;

def searchFunction(inp):
	animeNameLink = sc.pageSearch(inp);
	messageToSend = "";
	c = 1;
	for i in animeNameLink:
		messageToSend = messageToSend + str(c) + ": "+ i[0] + "\n";
		c+=1;
	return messageToSend;

def getAnimeFunction():
	messageToSend = currentAnimeNameLink[0];
	return messageToSend;

def animeFunction(inp):
	currentAnimeNameLink = animeNameLink[inp-1];
	return getAnimeFunction();


@client.event
async def on_ready():
	print("Bot is ready.");

@client.event
async def on_message(message):
	if message.author == client.user:
		return


	if message.content.startswith(search):
		inp = message.content[len(search):];
		messageToSend = searchFunction(inp)
		await message.channel.send(messageToSend);

	if message.content.startswith(srch):
		inp = message.content[len(srch):];
		messageToSend = searchFunction(inp)
		await message.channel.send(messageToSend);

	if message.content.startswith(currentanime):
		messageToSend = currentAnimeFunction();
		await message.channel.send(messageToSend);

	if message.content.startswith(ca):
		messageToSend = currentAnimeFunction();
		await message.channel.send(messageToSend);




client.run(RIRIKSU);
