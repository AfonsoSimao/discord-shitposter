import asyncio
import Utils.MessagingUtils as Msg
import Configs.ImageFolders as ImageFolders

async def no_reply(ctx):
	await Msg.send_random_image(ctx, ImageFolders.NO_FOLDER)

	
async def sorry_reply(ctx):
	await ctx.send("I'm sorry, master doesn't want me to talk to you right now...")
	await Msg.send_random_image(ctx, ImageFolders.SORRY_FOLDER)

