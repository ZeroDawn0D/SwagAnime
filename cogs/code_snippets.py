import cogs.scraper as sc
import discord;
currentAnimeNameLink = ("","");
currentSongNameLink = ("","");
OPEDOT = 0;
COLOUR = 0x7c7ccc;

animeNameLink = list();
songNameLink = list();

def songFunction(inp):
	global OPEDOT;
	global currentSongNameLink;
	global songNameLink;
	index = sc.readSongQuery(inp, OPEDOT) - 1;
	currentSongNameLink = songNameLink[index];

	lyr = sc.extractLyrics(currentSongNameLink[1]);

	return (lyr, currentAnimeNameLink[0]);


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

	return (songNameLink[:OPEDOT[2]][0], songNameLink[OPEDOT[2]:][0]);


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