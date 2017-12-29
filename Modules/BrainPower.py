
import asyncio
import Checks.AccessChecks as AccessChecks

from discord.ext import commands
from Exceptions.ReplyingException import ReplyingException

BRAIN_POWAH = '<:kreygasm:379629578764681227>O-oooooooooo AAAAE-A-A-I-A-U- \n<:kreygasm:379629578764681227>JO-oooooooooooo AAE-O-A-A-U-U-A- \n<:kreygasm:379629578764681227>E-eee-ee-eee AAAAE-A-E-I-E-A- \n<:kreygasm:379629578764681227>JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA'


class BrainPower():
	def __init__(self, bot):
		self.bot = bot
		
	##Commands

	@commands.command(name = 'brainpower')
	@commands.check(AccessChecks.check_passive_mode)
	async def brain_power(self):
		await self.bot.say(BRAIN_POWAH)

	##
	
	@brain_power.error
	async def on_brain_power_error(self, error, ctx):
		if isinstance(error, ReplyingException):
			await error.MessageCommand(ctx.bot)
	
def setup(bot):
	bot.add_cog(BrainPower(bot))
	

	
	