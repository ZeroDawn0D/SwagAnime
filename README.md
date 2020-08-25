animeNameLink = pageSearch(input("Enter anime: "));

c = 1;
for i in animeNameLink:
	print(str(c) + ": " + i[0]);
	c+=1;

songNameLink = openAnimePage(animeNameLink[int(input("Enter choice: "))-1][1]);


OPEDOT = headerDataGen(songNameLink);

c = 1;
for i in songNameLink:
	if i[1]=="#":
		print(i[0]);
		c = 1;
	else:
		print(str(c) +": "+i[0]);
		c+=1;

ans = input("Song query: ");

songIndex = readSongQuery(ans,OPEDOT) - 1;

print("SONG CHOSEN: " + songNameLink[songIndex][0]);

ls = extractLyrics(songNameLink[songIndex][1]);

for i in ls:
	print("\"" + i + "\"");