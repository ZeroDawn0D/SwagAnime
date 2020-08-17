# In search:
# Movie list: id #titlelist
# Song list: id #songlist
# span class .homesongs a class .list-group-items
#
from bs4 import BeautifulSoup;
import requests;
def getOddIndex(i):
	return 2*i+1;
def removeBreaks(str): #Remove newlines and trailing spaces
	newstr = "";
	for c in str:
		if(c!="\n"):
			newstr = newstr + c;
	return newstr.strip();


BASE_URL = "https://www.animesonglyrics.com/";
RESULTS = "results";
q = input("enter name: ");
q.strip();
q = '+'.join(q.split());
SEARCH = BASE_URL+RESULTS;
query = {"q":q};
print(SEARCH);
r = requests.get(SEARCH,params = query)
soup = BeautifulSoup(r.content, 'html.parser');
titlelist = soup.find(id = "titlelist");
achild = titlelist.findChildren("a", recursive = "True");
def getNameLink(a): #pass 'a' tag object, get Name and Link
	return (removeBreaks(a.get_text()), a['href']);
for i in achild:
	(a,b) = getNameLink(i);
	print(a);
	