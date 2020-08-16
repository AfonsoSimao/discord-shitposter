from Exceptions.ReplyingException import ReplyingException
import Replies.ExceptionReplies as Replies
import Configs.Constants as Constants

from discord.ext.commands import check

def isMaster():
	async def predicate(ctx):
		if ctx.author.id != Constants.ME or not await ctx.bot.is_owner(ctx.author):
			raise ReplyingException(Replies.no_reply)
		return True

	return check(predicate)
	
def check_passive_mode():
	
	async def predicate(ctx):
		if not ctx.bot.PASSIVE_MODE == 0:
			raise ReplyingException(Replies.sorry_reply)
		
		return True

	return check(predicate)