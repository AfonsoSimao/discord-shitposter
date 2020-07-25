
import asyncio
import re
import Utils.MessagingUtils as MsgUtils
import Configs.RegEx as REGEX
import Checks.AccessChecks as AccessChecks

from discord.ext import commands
from discord import Member
from Exceptions.ReplyingException import ReplyingException
from Storage.KeyValueStorage import KeyValueStorage

class LinkArchive(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.storage = KeyValueStorage('Storage/TinyDB/LinkRepository.json', True)

	#region Listeners

	@commands.Cog.listener()
	async def on_message(self, message):
		if not message.author.bot and not message.content.startswith('!'):
			mText = message.content
			urls = re.findall(REGEX.URL, mText, re.IGNORECASE)
			if len(urls) > 0:
				for url in urls:
					mText = mText.replace(url, '<{}>'.format(url))
				self.storage.add_value(message.author.id, mText)
	#endregion

	##Commands

	@commands.command(name = 'show_links', pass_context=True)
	async def show_links(self, ctx, user:Member=None):
		"""[<@user>] Shows links posted by the mentioned user."""
		try:
			if user is None:
				linkList = "User not found."
			else:
				
				foundLinks = self.storage.get(user.id) if user is not None else None
				
				if foundLinks is not None and len(foundLinks) > 0:
					linkList = "Links by {}\n".format(user.nick if user.nick is not None else user.name)
					for item in foundLinks:
						if (len(linkList) + len(item)) >= 2000:
							await ctx.author.send(linkList)
							linkList = ""
						linkList += "- {}\n".format(item)

				else:
					linkList = "No links found for user {}".format(user.nick if user.nick is not None else user.name)
			
			await ctx.author.send(linkList)
		except:
			print ("Unexpected error")
	##


def setup(bot):
	bot.add_cog(LinkArchive(bot))
