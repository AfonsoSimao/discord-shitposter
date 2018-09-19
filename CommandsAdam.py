
import asyncio
import Configs.MyCreds as MyCreds
import Checks.AccessChecks as AccessChecks

from discord.ext import commands
from Exceptions.ReplyingException import ReplyingException

startup_extensions = ["GreenText", "Polls.Poll", "LinkArchive"]
#startup_extensions = ["GreenText", "Polls.Poll", "Sandbox", "MAL.MALController", "LinkArchive"]

client = commands.Bot(command_prefix='!')

##Events

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	client.PASSIVE_MODE = 0

##

##Commands

@client.command(hidden=True)
@commands.check(AccessChecks.isMaster)
async def load(extension_name : str):
	"""Loads an extension."""
	try:
		client.load_extension("Modules."+extension_name)
	except (AttributeError, ImportError) as e:
		await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
		return
	await client.say("{} loaded.".format(extension_name))

@client.command(hidden=True)
@commands.check(AccessChecks.isMaster)
async def unload(extension_name : str):
	"""Unloads an extension."""
	client.unload_extension("Modules."+extension_name)
	await client.say("{} unloaded.".format(extension_name))

@client.command(hidden=True)
@commands.check(AccessChecks.isMaster)
async def reload(extension_name : str):
	"""Reloads an extension."""
	try:
		client.unload_extension("Modules."+extension_name)
		client.load_extension("Modules."+extension_name)
	except (AttributeError, ImportError) as e:
		await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
		return
	await client.say("{} reloaded.".format(extension_name))


@client.command(name='rstatus', hidden=True)
@commands.check(AccessChecks.isMaster)
async def reset_status_command():
	await client.change_presence() #no parameter means not playing anything

@client.command(name='passive_mode', hidden=True)
@commands.check(AccessChecks.isMaster)
async def on_passive_command(message):
	client.PASSIVE_MODE = int(message.strip())
	print('Passive mode {}engaged'.format('dis' if client.PASSIVE_MODE == 0 else ''))

##

##Error Handlers

@on_passive_command.error
async def on_passive_command_error(error, ctx):
	if isinstance(error, ReplyingException):
		await error.MessageCommand(client)

##

if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			client.load_extension("Modules."+extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))


	client.run(MyCreds.DiscordAdamToken)
