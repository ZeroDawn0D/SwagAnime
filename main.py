# In search:
# Movie list: id #titlelist
# Song list: id #songlist
# span class .homesongs a class .list-group-items
#
from bs4 import BeautifulSoup;
import requests;
def getOddIndex(i):
	return 2*i+1;



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
while 1:
	ans = int(input("enter index: "));
	if (ans==-1):
		break;
	titlelist = soup.find(id = "titlelist").contents;
	print(titlelist[getOddIndex(ans)]);
	linktag = titlelist[getOddIndex(ans)].a;
	link = linktag['href'];
	print(link);
	name = linktag.contents[2];
	print(name);