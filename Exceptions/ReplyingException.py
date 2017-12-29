from discord.ext import commands

class ReplyingException(commands.CheckFailure):
	def __init__(self, MessageCommand, textMessage = 'A ReplyingException was raised.'):
		super().__init__(textMessage)
		self.MessageCommand = MessageCommand