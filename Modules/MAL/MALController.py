
import asyncio
import Checks.AccessChecks as AccessChecks
import Modules.MAL.Views.SearchResultView as MALResultFormatter

from discord.ext import commands
from Modules.MAL.AnimeDAL import AnimeDAL
from Exceptions.ReplyingException import ReplyingException


class MAL():
	def __init__(self, bot):
		self.bot = bot
		self.search_service = AnimeDAL()
		
	##Commands

	@commands.command()
	@commands.check(AccessChecks.check_passive_mode)
	async def anime(self, *, message):
		await self.bot.say(**(MALResultFormatter.format_anime(self.search_service.get_anime(message.strip()))))
		
		
	@commands.command()
	@commands.check(AccessChecks.check_passive_mode)
	async def manga(self, *, message):
		await self.bot.say(**(MALResultFormatter.format_manga(self.search_service.get_manga(message.strip()))))

	##
	
	@anime.error
	@manga.error
	async def on_anime_error(self, error, ctx):
		if isinstance(error, ReplyingException):
			await error.MessageCommand(ctx.bot)
	
def setup(bot):
	bot.add_cog(MAL(bot))
	

	
	