from Exceptions.ReplyingException import ReplyingException
import Replies.ExceptionReplies as Replies
import Configs.Constants as Constants

def isMaster(ctx):
	if ctx.message.author.name != Constants.ADMIN_NAME:
		print("not master!")
		raise ReplyingException(Replies.no_reply)
		
	return True
	
def check_passive_mode(ctx):
	
	if not ctx.bot.PASSIVE_MODE == 0:
		raise ReplyingException(Replies.sorry_reply)
	
	return True