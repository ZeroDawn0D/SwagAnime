import discord;
from discord.ext import commands;
import os;
import scraper as sc;

RIRIKSU = os.environ.get("RIRIKSU");
client = commands.Bot(command_prefix= ">");
COLOUR = 0x7c7ccc;
info = ">info"; i = ">i"; # bot info
search = ">search "; srch = ">sr "; # anime name search IMPLEMENTED
song = ">song ";s = ">s "; # choose song IMPLEMENTED
anime = ">anime ";a = ">a "; # choose anime IMPLEMENTED
currentanime = ">currentanime";ca = ">ca"; #current anime list IMPLEMENTED
currentsong = ">currentsong"; cs = ">cs"; #current song list IMPLEMENTED
getanime = ">getanime";ga = ">ga"; #get current chosen anime IMPLEMENTED


currentAnimeNameLink = ("","");
currentSongNameLink = ("","");
OPEDOT = 0;


animeNameLink = list();
songNameLink = list();

def songFunction(inp):
	global OPEDOT;
	global currentSongNameLink;
	global songNameLink;
	index = sc.readSongQuery(inp, OPEDOT) - 1;
	currentSongNameLink = songNameLink[index];

	lyr = sc.extractLyrics(currentSongNameLink[1]);

	messageToSend = "";

	for i in lyr:
		messageToSend = messageToSend + i + "\n";

	embed = discord.Embed(
		title = "Song",
		description = messageToSend,
		colour  = COLOUR
	)
	return embed;


def currentAnimeListFunction():
	global animeNameLink;
	messageToSend = "";
	c = 1;
	for i in animeNameLink:
		messageToSend = messageToSend + str(c) + ": "+ i[0] + "\n";
		c+=1;
	embed = discord.Embed(
		title = "Current Anime List",
		description = messageToSend,
		colour  = COLOUR
	)
	return embed;

def searchFunction(inp):
	global animeNameLink;
	animeNameLink = sc.pageSearch(inp);
	return currentAnimeListFunction();


def currentAnimeFunction():
	global currentAnimeNameLink;
	messageToSend = currentAnimeNameLink[0];
	embed = discord.Embed(
		title = "Current Anime",
		description = messageToSend,
		colour  = COLOUR
	)
	return embed;

def currentSongListFunction():
	global songNameLink;
	messageToSend = "";
	c = 1;
	for i in songNameLink:
		if i[1]=="#":
			messageToSend = messageToSend + i[0] + "\n";
			c = 1;
		else:
			messageToSend = messageToSend + str(c) +": "+i[0] + "\n";
			c+=1;

	embed = discord.Embed(
		title = "Current Song List",
		description = messageToSend,
		colour  = COLOUR
	)
	return embed;


def animeFunction(inp):
	global currentAnimeNameLink;
	global animeNameLink;
	global songNameLink;
	global OPEDOT;
	currentAnimeNameLink = animeNameLink[int(inp)-1];
	songNameLink = sc.openAnimePage(currentAnimeNameLink[1]);
	OPEDOT = sc.headerDataGen(songNameLink);
	return currentSongListFunction();

def helpFunction():
	embed = discord.Embed(
		title = "TEST",
		description = "TEST DESC",
		colour  = 0x7c7ccc
	)
	return embed;

@client.command()
async def search(ctx, args):
	await ctx.send(embed = searchFunction(args));

@client.command()
async def sr(ctx, args):
	await search(ctx,args);

@client.command()
async def currentanimelist(ctx, args):
	await ctx.send(embed = currentAnimeListFunction(args));

@client.command()
async def cal(ctx, args):
	await currentanimelist(ctx,args);

@client.command()
async def anime(ctx, args):
	await ctx.send(embed = animeFunction(args));

@client.command()
async def a(ctx,args):
	await anime(ctx,args);

@client.command()
async def song(ctx,args):
	await ctx.send(embed = songFunction(args));

@client.command()
async def s(ctx, args):
	await song(ctx, args);

@client.command()
async def currentsonglist(ctx,args):
	await ctx.send(embed = currentSongListFunction(args));

@client.command()
async def csl(ctx, args):
	await currentsonglist(ctx,args);

@client.command()
async def currentanime(ctx, args):
	await ctx.send(embed = currentAnimeFunction(args));

@client.command()
async def ca(ctx, args):
	await currentanime(ctx, args);

@client.command()
async def info(ctx, args):
	pass;

@client.event
async def on_ready():
	print("Bot is ready.");



client.run(RIRIKSU);
