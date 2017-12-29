import asyncio
import Utils.MessagingUtils as Msg
import Configs.ImageFolders as ImageFolders
##exception replies

async def no_reply(client):
	await Msg.send_random_image(client, ImageFolders.NO_FOLDER)

	
async def sorry_reply(client):
	await client.say("I'm sorry, master doesn't want me to talk to you right now...")
	await Msg.send_random_image(client, ImageFolders.SORRY_FOLDER)

##