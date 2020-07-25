import asyncio
import os
from random import choice

from discord import File as DiscordFile

async def send_random_image(ctx, folder, channel=None):
	selectedImage = choice(os.listdir(folder))
	print(u'sending {}...'.format(selectedImage))
	
	await ctx.send(file = DiscordFile('{}\\{}'.format(folder, selectedImage), filename=selectedImage))