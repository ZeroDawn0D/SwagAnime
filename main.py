
from bs4 import BeautifulSoup;
from bs4 import element as bs4elem;
import requests;
import os;

BASE_URL = "https://www.animesonglyrics.com/";
SEARCH = BASE_URL+"results";
RIRIKSU = os.environ.get("RIRIKSU");
#Remove newlines and trailing spaces

def removeBreaks(str):
	newstr = "";
	for c in str:
		if(c!="\n"):
			newstr = newstr + c;
	return newstr.strip();

#pass 'a' tag object, get Name and Link
def getNameLink(a):
	return (removeBreaks(a.get_text()), a['href']);

# In search:
# Movie list: id #titlelist
# Song list: id #songlist
# a -> href(link) text(anime/song name)
# TODO: fix song name 

#uses the page's search function to generate a list of anime or songs
#and the links to their pages. 
#returns an array of tuples animeNameLink containing data as (name,link)
def pageSearch(query = "", listtype = "A"): 
	idType = "";
	if listtype == "A":
		idType = "titlelist";
	elif listtype == "S":
		idType = "songlist";
	else:
		print("wrongChoice");
		return;
	param = {"q":query};
	r = requests.get(SEARCH, params = param);
	soup = BeautifulSoup(r.content, 'html.parser');
	mainlist = soup.find(id = idType);
	achild = mainlist.findChildren("a", recursive = "True");
	animeNameLink = [('','')] * len(achild);
	c = 0;
	for i in achild:
		animeNameLink[c] = getNameLink(i);
		#if listtype == "S":
		#	nameLink[c] = (formatSongName(nameLink[c][0]),nameLink[c][1]);
		c+=1;
	return animeNameLink;

#id #songlist
# heading -> href = '#'
#returns an array of tuples songNameLink containing data as (name,link)
def openAnimePage(pageLink):
	r = requests.get(pageLink);
	soup = BeautifulSoup(r.content, 'html.parser');
	mainlist = soup.find(id = "songlist");
	achild = mainlist.findChildren("a", recursive = "True");
	songNameLink = [('','')] * len(achild);
	c = 0;
	for i in achild:
		songNameLink[c] = getNameLink(i);
		songNameLink[c] = (' '.join(songNameLink[c][0].split()),songNameLink[c][1]);
		c+=1;
	return songNameLink;

# a .SngLnk2 -> song name
# span .songartist -> a -> artist name
# #tablyrics #tab1 -> romaji #tab2 -> english #tab3 -> kanji
# returns lyrics
def extractLyrics(pageLink):
	r = requests.get(pageLink);
	soup = BeautifulSoup(r.content, 'html.parser');
	kanjiObject = soup.find(id = "tab1");
	lyricsString = [];
	for i in kanjiObject.contents:
		if(isinstance(i, bs4elem.NavigableString)):
			lyricsString.append(i);
	lyricsString[0] = removeBreaks(lyricsString[0]);
	return lyricsString;

#generates the array position of Opening, Closing and Other headers
def headerDataGen(songNameLink):
	OP = ED = OT = 0;
	c = 1;
	for i in songNameLink:
		if i[1]=='#':
			if i[0] == "Opening Themes":
				OP = c;
			elif i[0] == "Ending Themes":
				ED = c;
			elif i[0] == "Other Songs":
				OT = c;
		c+=1;
	last = len(songNameLink) - 1;
	return (OP,ED,OT);

def readSongQuery(query, OPEDOT):
	(OP,ED,OT) = OPEDOT;
	pos = -1;
	ql = query.split();
	type = ql[0];
	if type=="OP":
		pos = OP;
	elif type=="ED":
		pos = ED;
	elif type=="OT";
		pos = OT;
	
	pos += str(ql[1]);
	return pos;

#--------------------------------X----------------------------------------



animeNameLink = pageSearch(input("Enter anime: "));

c = 1;
for i in animeNameLink:
	print(str(c) + ": " + i[0]);
	c+=1;

songNameLink = openAnimePage(animeNameLink[int(input("Enter choice: "))-1][1]);

c = 1;
for i in songNameLink:
	print(str(c) + ": " + i[0]);
	c+=1;

OPEDOT = headerDataGen(songNameLink);