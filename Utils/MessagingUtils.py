import asyncio
import os
from random import choice

async def send_random_image(client, folder, channel=None):
	selectedImage = choice(os.listdir(folder))
	print(u'sending {}...'.format(selectedImage))
	if channel is None:
		await client.upload('{}\\{}'.format(folder, selectedImage))
	else: 
		await client.send_file(channel, '{}\\{}'.format(folder, selectedImage))