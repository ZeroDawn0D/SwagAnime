# In search:
# Movie list: id #titlelist
# Song list: id #songlist
# a -> href(link) text(anime/song name)
# TODO: fix song name 
from bs4 import BeautifulSoup;
import requests;

BASE_URL = "https://www.animesonglyrics.com/";
SEARCH = BASE_URL+"results";

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

#uses the page's search function to generate a list of anime or songs
#and the links to thier pages
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
	global nameLink;
	nameLink = [('','')] * len(achild);
	c = 0;
	for i in achild:
		nameLink[c] = getNameLink(i);
		#if listtype == "S":
		#	nameLink[c] = (formatSongName(nameLink[c][0]),nameLink[c][1]);
		c+=1;





q = input("enter anime: ");
q.strip();
q = '+'.join(q.split());
listtype = input("enter type: (A)nime/(S)ong: ").upper();
listtype.strip();

pageSearch(q,listtype);
c = 0;
for i in nameLink:
	print(str(c+1) + ": " + i[0]);
	c+=1;