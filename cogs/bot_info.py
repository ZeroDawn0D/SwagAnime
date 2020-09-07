from discord.ext.commands import Cog, command;
import discord
from cogs.code_snippets import *;
COLOUR = 0x7c7ccc;
class BotInfo(Cog):
	def __init__(self,bot):
		self.bot = bot;
		self.prefix = '>';

	@command(aliases = ['sr','srch'])
	async def search(self,ctx, args):
		await ctx.send(embed = searchFunction(args));

	@command(aliases = ['cal'])
	async def currentanimelist(self,ctx, args):
		await ctx.send(embed = currentAnimeListFunction(args));

	@command(aliases = ['a'])
	async def anime(self, ctx, args):
		await ctx.send(embed = animeFunction(args));

	@command(aliases = ['s'])
	async def song(self,ctx,args):
		(lyr,songName) = songFunction(args);
		c = 0; div = len(lyr);
		for i in lyr:
			if i.startswith("[F"):
				div = c;
				break;
			c+=1;
		lyr1 = lyr[:div];
		lyr2 = lyr[div+1:];
		
		mts1 = "";
		for i in lyr1:
			mts1 = mts1 + i + "\n";
		embed1 = discord.Embed(
				title = songName,
				description = mts1,
				colour = COLOUR
			);
		mts2 = "";
		for i in lyr2:
			mts2 = mts2 + i + "\n";
		embed2 = discord.Embed(
				title = "[Full Version]",
				description = mts2,
				colour = COLOUR
			);
		await ctx.send(embed = embed1);
		await ctx.send(embed = embed2);

	@command(aliases = ['csl'])
	async def currentsonglist(self,ctx,args):
		await ctx.send(embed = currentSongListFunction(args));


	@command(aliases = ['ca'])
	async def currentanime(self,ctx, args):
		await ctx.send(embed = currentAnimeFunction(args));


	@command(aliases = ['i'])
	async def info(self,ctx):
		pass;
