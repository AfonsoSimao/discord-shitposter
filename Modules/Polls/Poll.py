import asyncio
import Checks.AccessChecks as AccessChecks
import Utils.MessagingUtils as MsgUtils
import Configs.ImageFolders as ImageFolders

from discord.ext import commands
from Exceptions.ReplyingException import ReplyingException
from Modules.Polls.PollDAL import PollBuilder as PollDAL

PollService = PollDAL()

class Poll():
	PollService = None
	
	def __init__(self, bot):
		self.bot = bot
		
	##Commands

	@commands.command(pass_context=True)
	async def add_poll(self, ctx, *, message):
		"""<poll_text> Creates a new poll."""
		pollId = PollService.add_poll(message.strip(), ctx.message.author.name)
		print("Poll Created!")
		print(message.strip())
		await self.bot.say("Poll Created! (Id: {})".format(pollId))
		
	@commands.command(pass_context=True)
	async def close(self, ctx, pollid):
		"""<poll_id> Closes an existing poll."""
		final_result = PollService.close_poll(int(pollid), ctx.message.author.name)
		if final_result == PollDAL.POLL_NOT_FOUND:
			await self.bot.say("As if such a poll would exist...")
		elif final_result == PollDAL.NOT_OP:
			await MsgUtils.send_random_image(self.bot, ImageFolders.NO_FOLDER)
		elif final_result == PollDAL.POLL_CLOSED:
			await MsgUtils.send_random_image(self.bot, ImageFolders.POLL_FOLDER)
		else:
			print("{} Closed with {} Yes vs {} No".format(final_result['poll'], len(final_result['yes']), len(final_result['no'])))
			await self.bot.say("'{}' Closed with {} Yes vs {} No".format(final_result['poll'], len(final_result['yes']), len(final_result['no'])))
		
	@commands.command(pass_context=True)
	async def yes(self, ctx, pollid):
		"""<poll_id> Votes 'yes' on a poll."""
		status = PollService.add_vote(ctx.message.author.name, 'yes', int(pollid))
		if status == 0:
			print("Vote Accepted!")
			await self.bot.say("Vote Accepted!")
		elif status == PollDAL.MULTIPLE_VOTE:
			await self.bot.say("Please do not vote more than once >.<")
		elif status == PollDAL.POLL_NOT_FOUND:
			await self.bot.say("As if such a poll would exist...")
		elif status == PollDAL.POLL_CLOSED:
			await MsgUtils.send_random_image(self.bot, ImageFolders.POLL_FOLDER)
		
	@commands.command(pass_context=True)
	async def no(self, ctx, pollid):
		"""<poll_id> Votes 'no' on a poll."""
		status = PollService.add_vote(ctx.message.author.name, 'no', int(pollid))
		
		if status == 0:
			print("Vote Accepted!")
			await self.bot.say("Vote Accepted!")
		elif status == PollDAL.MULTIPLE_VOTE:
			await self.bot.say("Please do not vote more than once >.<")
		elif status == PollDAL.POLL_NOT_FOUND:
			await self.bot.say("As if such a poll would exist...")
		elif status == PollDAL.POLL_CLOSED:
			await MsgUtils.send_random_image(self.bot, ImageFolders.POLL_FOLDER)
		
	@commands.command()
	async def list_polls(self):
		"""Shows all open polls."""
		activePolls = PollService.list_open_polls()
		
		if activePolls is not None:
			pollList = "```"
			for item in activePolls:
				pollList += "{}. {}:'{}'\n".format(item.doc_id, item["created_by"], item['poll'])
			pollList += "```"
		
		await self.bot.say(pollList)
		
	@commands.command()
	async def poll_standing(self, pollid):
		"""<poll_id> Shows the specified poll and its results."""
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