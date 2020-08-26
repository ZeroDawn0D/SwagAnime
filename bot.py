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
OPEDOT = 0;


animeNameLink = list();
songNameLink = list();



def currentAnimeFunction():
	global animeNameLink;
	messageToSend = "";
	c = 1;
	for i in animeNameLink:
		messageToSend = messageToSend + str(c) + ": "+ i[0] + "\n";
		c+=1;
	return messageToSend;

def searchFunction(inp):
	global OPEDOT
	global animeNameLink;
	animeNameLink = sc.pageSearch(inp);
	return currentAnimeFunction();

def getAnimeFunction():
	global currentAnimeNameLink;
	messageToSend = currentAnimeNameLink[0];
	return messageToSend;

def animeFunction(inp):
	global currentAnimeNameLink;
	global animeNameLink;
	currentAnimeNameLink = animeNameLink[int(inp)-1];
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

	if message.content.startswith(anime):
		inp = message.content[len(anime):];
		messageToSend = animeFunction(inp);
		await message.channel.send(messageToSend);

	if message.content.startswith(a):
		inp = message.content[len(a):];
		messageToSend = animeFunction(inp);
		await message.channel.send(messageToSend);




client.run(RIRIKSU);
