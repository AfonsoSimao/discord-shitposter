
import asyncio
import Configs.MyCreds as MyCreds
import Checks.AccessChecks as AccessChecks

from discord.ext import commands
from Exceptions.ReplyingException import ReplyingException

startup_extensions = ["GreenText", "LinkArchive", "MAL.MALController"]
#startup_extensions = ["GreenText", "Polls.Poll", "Sandbox", "MAL.MALController", "LinkArchive"]

client = commands.Bot(command_prefix='!')

#region Events

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	client.PASSIVE_MODE = 0

@client.event
async def on_command_error(ctx, error):
	"""All CommandErrors end up here."""

	if isinstance(error, ReplyingException):
		await error.MessageCommand(ctx)
	else:
		print(error)

#endregion

#region Commands

@client.command(hidden=True)
@AccessChecks.isMaster()
async def load(ctx, extension_name : str):
	"""Loads an extension."""
	try:
		client.load_extension("Modules."+extension_name)
	except (AttributeError, ImportError) as e:
		await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
		return
	await ctx.send("{} loaded.".format(extension_name))

@client.command(hidden=True)
@AccessChecks.isMaster()
async def unload(ctx, extension_name : str):
	"""Unloads an extension."""
	client.unload_extension("Modules."+extension_name)
	await ctx.send("{} unloaded.".format(extension_name))

@client.command(hidden=True)
@AccessChecks.isMaster()
async def reload(ctx, extension_name : str):
	"""Reloads an extension."""
	try:
		client.unload_extension("Modules."+extension_name)
		client.load_extension("Modules."+extension_name)
	except (AttributeError, ImportError) as e:
		await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
		return
	await ctx.send("{} reloaded.".format(extension_name))


@client.command(name='rstatus', hidden=True)
@AccessChecks.isMaster()
async def reset_status_command():
	await client.change_presence() #no parameter means not playing anything

@client.command(name='passive_mode', hidden=True)
@AccessChecks.isMaster()
async def on_passive_command(ctx, message):
	client.PASSIVE_MODE = int(message.strip())
	print('Passive mode {}engaged'.format('dis' if client.PASSIVE_MODE == 0 else ''))

#endregion


if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			client.load_extension("Modules."+extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))


	client.run(MyCreds.DiscordAdamToken)
