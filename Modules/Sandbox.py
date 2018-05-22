
import sys
import time
import asyncio
import Checks.AccessChecks as AccessChecks
from Storage.KeyValueStorage import KeyValueStorage

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
		try:
			db = KeyValueStorage("Storage/TinyDB/singlekv.json")
			succTests = 0
			print(db.exists("0123")) #False
			if not db.exists("0123"): succTests +=1
			db.add_value("0123", "user1")
			print(db.exists("0123")) #True
			if db.exists("0123"): succTests +=1
			print(db.get("0123")) #user1
			if db.get("0123") == "user1": succTests +=1
			db.add_value("0123", "user2")
			print(db.get("0123")) #user2
			if db.get("0123") == "user2": succTests +=1

		except Exception as e:
			print(e)
			await self.bot.say("Uhh... check the console.")
			return

		print("Test Complete!")
		await self.bot.say("{}/{} tests complete.".format(succTests, 4))


	##

	@test_db.error
	async def on_error(self, error, ctx):
		if isinstance(error, ReplyingException):
			await error.MessageCommand(ctx.bot)

def setup(bot):
	bot.add_cog(DevSandbox(bot))
