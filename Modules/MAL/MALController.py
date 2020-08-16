
import asyncio
import Checks.AccessChecks as AccessChecks
import Modules.MAL.Views.SearchResultView as MALResultFormatter

from discord.ext import commands
from Modules.MAL.AnimeDAL import AnimeDAL
from Exceptions.ReplyingException import ReplyingException


class MAL(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.search_service = AnimeDAL()
		
	#region Commands

	@commands.command()
	@AccessChecks.check_passive_mode()
	async def anime(self, ctx, *, message):
		entry = await self.search_service.get_anime(message.strip())
		await ctx.send(**(MALResultFormatter.format_anime(entry)))
		
		
	@commands.command()
	@AccessChecks.check_passive_mode()
	async def manga(self, ctx, *, message):
		entry = await self.search_service.get_manga(message.strip())
		await ctx.send(**(MALResultFormatter.format_manga(entry)))

	#endregion
	
def setup(bot):
	bot.add_cog(MAL(bot))
	

	
	