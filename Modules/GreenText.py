
import asyncio
import Utils.MessagingUtils as MsgUtils
import Configs.ImageFolders as ImageFolders
import Checks.AccessChecks as AccessChecks

from discord import Game
from discord import Emoji
from discord.ext import commands
from random import randint
from Exceptions.ReplyingException import ReplyingException


class GreenText(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.GreentextChance = 10
		self.TermsForGreentext = ['>mcq', '>tfw', '>mfw']
		self.REPLY_FOLDER = ImageFolders.REACTION_FOLDER

	#region private_methods

	async def __greentextan(self, ctx):
		msg = ctx.message.content if not ctx.message.content.startswith('>') else ctx.message.content[1:]
		await ctx.send(u'```css\n>{}\n```'.format(msg))
		await MsgUtils.send_random_image(ctx, self.REPLY_FOLDER)

	def __roll_for_greentext(self, message):
		isGreenTextan = randint(1, 100)
		print(u'{}: "{}" ({}/{}%)'.format(message.author.name, message.content, isGreenTextan, self.GreentextChance))
		chanceHit = isGreenTextan <= self.GreentextChance
		if chanceHit:
			self.GreentextChance = randint(1,10)

		return chanceHit or any(message.content.lower().startswith(term) for term in self.TermsForGreentext)

	#endregion

	#region Listeners

	@commands.Cog.listener()
	async def on_message(self, message):
		if not message.author.bot and not message.content.startswith('!') and len(message.content.strip()) > 1 and self.__roll_for_greentext(message):
			await self.__greentextan(await self.bot.get_context(message))
			#await self.bot.change_presence(game=Game(name='{} like a damn fiddle!'.format(message.author.name)))

	#endregion

	#region Commands

	@commands.command(name = 'setquoterate', hidden=True)
	@AccessChecks.isMaster()
	async def set_quote_rate(self, ctx, rate):
		self.GreentextChance = int(rate)
		print('GreenTextChance is now {}%'.format(self.GreentextChance))

	@commands.command(name = 'engage_smug_protocol', hidden=True)
	@AccessChecks.isMaster()
	async def smug_protocol(self, ctx):
		self.REPLY_FOLDER = ImageFolders.SMUG_FOLDER
		self.GreentextChance = 100
		print('Smug protocol engaged!')

	@commands.command(name = 'react', hidden=True)
	@AccessChecks.isMaster()
	async def react(self, ctx):
		#await self.bot.add_reaction(Emoji(name="ok_hand"))
		##await self.bot.add_reaction(self.bot.emojis.find("name", "joy"))
		##await self.bot.add_reaction(self.bot.emojis.find("name", "100"))
		pass
	#endregion

def setup(bot):
	bot.add_cog(GreenText(bot))
