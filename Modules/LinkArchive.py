
import asyncio
import re
import Utils.MessagingUtils as MsgUtils
import Configs.RegEx as REGEX
import Checks.AccessChecks as AccessChecks

from discord.ext import commands
from discord import User
from Exceptions.ReplyingException import ReplyingException
from Storage.KeyValueStorage import KeyValueStorage

class LinkArchive():
	def __init__(self, bot):
		self.bot = bot
		self.storage = KeyValueStorage('Storage/TinyDB/LinkRepository.json', True)

	##Listeners

	async def on_message(self, message):
		if not message.author.bot and not message.content.startswith('!'):
			mText = message.content
			urls = re.findall(REGEX.URL, mText, re.IGNORECASE)
			if len(urls) > 0:
				for url in urls:
					mText = mText.replace(url, '<{}>'.format(url))
				self.storage.add_value(message.author.id, mText)
	##

	##Commands

	@commands.command(name = 'show_links', pass_context=True)
	async def show_links(self, ctx, user:User=None):
		"""[<@user>] Shows links posted by the mentioned user."""
		u = user if user is not None else ctx.message.author
		foundLinks = self.storage.get(u.id)
		if foundLinks is not None and len(foundLinks) > 0:
			linkList = "Links by {}\n".format(u.nick if u.nick is not None else u.name)
			for item in foundLinks:
				linkList += "- {}\n".format(item)

		else:
			linkList = "No links found for user {}".format(u.nick if u.nick is not None else u.name)
		await self.bot.say(linkList)

	##

	@show_links.error
	async def on_passive_command_error(self, error, ctx):
		if isinstance(error, ReplyingException):
			await error.MessageCommand(ctx.bot)

def setup(bot):
	bot.add_cog(LinkArchive(bot))
