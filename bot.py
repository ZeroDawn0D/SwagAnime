from discord.ext.commands import Bot;
import os;
from cogs.bot_info import BotInfo 
RIRIKSU = os.environ.get("RIRIKSU");
client = Bot(command_prefix= ">");

"""
info = ">info"; i = ">i"; # bot info
search = ">search "; srch = ">sr "; # anime name search IMPLEMENTED
song = ">song ";s = ">s "; # choose song IMPLEMENTED
anime = ">anime ";a = ">a "; # choose anime IMPLEMENTED
currentanime = ">currentanime";ca = ">ca"; #current anime list IMPLEMENTED
currentsong = ">currentsong"; cs = ">cs"; #current song list IMPLEMENTED
getanime = ">getanime";ga = ">ga"; #get current chosen anime IMPLEMENTED
"""


client.add_cog(BotInfo(client));

@client.event
async def on_ready():
	print("Bot is ready.");


client.run(RIRIKSU);
