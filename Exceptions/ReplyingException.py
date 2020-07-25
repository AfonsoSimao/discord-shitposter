from discord.ext import commands

class ReplyingException(commands.CheckFailure):
	""" Use to perform a custom command (MessageCommand) on error handling instead of just printing a message """

	def __init__(self, MessageCommand, textMessage = 'A ReplyingException was raised.'):
		super().__init__(textMessage)
		self.MessageCommand = MessageCommand #MessageCommand receives a ctx as its only parameter