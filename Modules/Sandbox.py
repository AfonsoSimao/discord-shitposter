
import sys
import time
import asyncio
import Checks.AccessChecks as AccessChecks
from Modules.MAL.AnimeDAL import AnimeDAL
import Modules.MAL.Views.SearchResultView as MALResultFormatter

from discord.ext import commands
from Exceptions.ReplyingException import ReplyingException

class DevSandbox():

	def __init__(self, bot):
		self.bot = bot
		
	##Commands

	@commands.command(hidden=True)
	@commands.check(AccessChecks.isMaster)
	async def test_db(self):
		print("Starting Test_db...")
		
		dal = AnimeDAL()
	
		print("running AnimeDAL.get_anime for 'bleach'")
		
		res = dal.get_anime("bleach")
		print(res.title)
		
		await self.bot.say(**(MALResultFormatter.format_anime(res)))
		
		print("Test Complete!")
		
		
		await self.bot.say("{}/{} tests complete.".format(succTests, 1))
		
		
	##
	
	@test_db.error
	async def on_anime_error(self, error, ctx):
		if isinstance(error, ReplyingException):
			await error.MessageCommand(ctx.bot)
	
def setup(bot):
	bot.add_cog(DevSandbox(bot))