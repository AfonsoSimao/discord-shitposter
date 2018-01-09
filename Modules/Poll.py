import asyncio
import Checks.AccessChecks as AccessChecks

from discord.ext import commands
from Exceptions.ReplyingException import ReplyingException
from APIs.Polls.PollDAL import PollBuilder as PollDAL

PollService = PollDAL()

class Poll():
	PollService = None
	
	def __init__(self, bot):
		self.bot = bot
		
	##Commands

	@commands.command(pass_context=True)
	async def add_poll(self, ctx, *, message):
		"""<poll_text> Creates a new poll."""
		PollService.add_poll(message.strip(), ctx.message.author.name)
		print("Poll Created!")
		print(message.strip())
		await self.bot.say("Poll Created!")
		
	@commands.command(pass_context=True)
	async def yes(self, ctx, pollid):
		"""<poll_id> Votes 'yes' on a poll."""
		PollService.add_vote(ctx.message.author.name, 'yes', int(pollid))
		print("Vote Accepted!")
		await self.bot.say("Vote Accepted!")
		
	@commands.command(pass_context=True)
	async def no(self, ctx, pollid):
		"""<poll_id> Votes 'no' on a poll."""
		PollService.add_vote(ctx.message.author.name, 'no', int(pollid))
		print("Vote Accepted!")
		await self.bot.say("Vote Accepted!")
		
	@commands.command()
	async def list_polls(self):
		"""Shows all open polls."""
		activePolls = PollService.list_open_polls()
		
		if activePolls is not None:
			pollList = "```"
			for item in activePolls:
				pollList += "{}. {}\n".format(item.doc_id, item['poll'])
			pollList += "```"
		
		await self.bot.say(pollList)
		
	@commands.command()
	async def poll_standing(self, pollid):
		"""Shows the specified poll and its results."""
		selPollId = int(pollid)
		if selPollId is not None:
			selectedPoll = PollService.get_poll(int(pollid))
			
			if selectedPoll is not None:
				pollList = "```"
				pollList += "{}. {}\n".format(selectedPoll.doc_id, selectedPoll['poll'])
				pollList += "Yes: {}\n".format(len(selectedPoll['yes']))
				pollList += "No: {}\n".format(len(selectedPoll['no']))
				pollList += "```"
			
			await self.bot.say(pollList)
	
	@add_poll.error
	async def on_poll_error(self, error, ctx):
		if isinstance(error, ReplyingException):
			await error.MessageCommand(ctx.bot)
		
		

def setup(bot):
	bot.add_cog(Poll(bot))