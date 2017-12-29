
import asyncio
import Utils.MessagingUtils as MsgUtils
import Configs.ImageFolders as ImageFolders
import Checks.AccessChecks as AccessChecks

from discord import Game
from discord import Emoji
from discord.ext import commands
from random import randint
from Exceptions.ReplyingException import ReplyingException



async def greentextan(client, message):
	msg = message.content if not message.content.startswith('>') else message.content[1:]
	await client.send_message(message.channel, u'```css\n>{}\n```'.format(msg))
	await MsgUtils.send_random_image(client, ImageFolders.REACTION_FOLDER, message.channel)
	
def roll_for_greentext(client, message):
	isGreenTextan = randint(1, 100)
	print(u'{}: "{}" ({}/{}%)'.format(message.author.name, message.content, isGreenTextan, client.GreentextChance))
	chanceHit = isGreenTextan <= client.GreentextChance
	if chanceHit:
		client.GreentextChance = randint(1,10)
	##if isGreenTextan == 1
		
	return chanceHit or any(message.content.lower().startswith(term) for term in client.TermsForGreentext)
	

	
class GreenText():
	def __init__(self, bot):
		self.bot = bot
		bot.GreentextChance = 10
		bot.TermsForGreentext = ['>mcq', '>tfw', '>mfw']
		
	##Listeners

	async def on_message(self, message):
		
		if not message.author.bot and not message.content.startswith('!') and len(message.content.strip()) > 1 and roll_for_greentext(self.bot, message):
			await greentextan(self.bot, message)
			await self.bot.change_presence(game=Game(name='{} like a damn fiddle!'.format(message.author.name)))
			
	##

	##Commands

	@commands.command(name = 'setquoterate')
	@commands.check(AccessChecks.isMaster)
	async def set_quote_rate(self, rate):
		self.bot.GreentextChance = int(rate)
		print('GreenTextChance is now {}%'.format(self.bot.GreentextChance))

	@commands.command(name = 'react')
	@commands.check(AccessChecks.isMaster)
	async def react(self):
		await self.bot.add_reaction(Emoji(name="ok_hand"))
		##await self.bot.add_reaction(self.bot.emojis.find("name", "joy"))
		##await self.bot.add_reaction(self.bot.emojis.find("name", "100"))
		
	##
	
	@set_quote_rate.error
	async def on_passive_command_error(self, error, ctx):
		if isinstance(error, ReplyingException):
			await error.MessageCommand(ctx.bot)
	
def setup(bot):
	bot.add_cog(GreenText(bot))
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	