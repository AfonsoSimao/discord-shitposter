from discord import Embed
import asyncio
import Checks.AccessChecks as AccessChecks
import Configs.MyCreds as MyCreds
import Views.MAL.SearchResultView as MALResultFormatter

from discord.ext import commands
from APIs.MAL.AnimeSearch import MALSearchAPI as MALAPI
from Exceptions.ReplyingException import ReplyingException

MALSearchService = MALAPI(MyCreds.MALUser, MyCreds.MALPassword)

def search_mal_anime(query):
	print("Query:{}".format(query))
	return MALResultFormatter.format_anime(MALSearchService.search_anime(query))
	
def search_mal_manga(query):
	print("Query:{}".format(query))
	return MALResultFormatter.format_manga(MALSearchService.search_manga(query))


class MAL():
	MALSearchService = None

	def __init__(self, bot):
		self.bot = bot
		
	##Commands

	@commands.command()
	@commands.check(AccessChecks.check_passive_mode)
	async def anime(self, *, message):
		response = search_mal_anime(message.strip())
		print(response)
		#embed = Embed(title="Title", description="Desc", color=0x00ff00)
		#embed.set_image(url="https://myanimelist.cdn-dena.com/images/anime/2/75259.jpg")
		#embed.add_field(name="Field1", value="hi", inline=False)
		#embed.add_field(name="Field2", value="hi2", inline=True)
		await self.bot.say('',embed=response)#, embed=embed)
		
	@commands.command()
	@commands.check(AccessChecks.check_passive_mode)
	async def manga(self, *, message):
		response = search_mal_manga(message.strip())
		print(response)
		await self.bot.say(response)

	##
	
	@anime.error
	@manga.error
	async def on_anime_error(self, error, ctx):
		if isinstance(error, ReplyingException):
			await error.MessageCommand(ctx.bot)
	
def setup(bot):
	bot.add_cog(MAL(bot))
	

	
	