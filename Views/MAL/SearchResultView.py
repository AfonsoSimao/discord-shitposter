import xml.etree.ElementTree as ET
from discord import Embed

def format_anime(element):
	if element is None:
		return 'No Results Found! (You fucking normie...)'
	
	#responseView = "https://myanimelist.net/anime/{}\n".format(element.find('id').text)
	
	desc = element.find('english').text if element.find('english') is not None else ''
	
	embed = Embed(title=element.find('title').text, description=desc, color=0x00ff00, url="https://myanimelist.net/anime/{}\n".format(element.find('id').text))
	embed.set_thumbnail(url=element.find('image').text)
	#embed.set_image(url="https://myanimelist.cdn-dena.com/images/anime/2/75259.jpg")
	embed.add_field(name="Type", value=element.find('type').text, inline=True)
	embed.add_field(name="Status", value=element.find('status').text, inline=True)
	embed.add_field(name="Episodes", value=element.find('episodes').text, inline=True)
	embed.add_field(name="Score", value=element.find('score').text, inline=True)
	
	embed.set_footer(text = element.find('synopsis').text)
	
	
	#responseView += "```{}\n".format(element.find('title').text)
	#responseView += "Avg. Score: {}\n".format(element.find('score').text)
	#responseView += "{} Episodes\n".format(element.find('episodes').text)
	#responseView += "Type: {}\n".format(element.find('type').text)
	#responseView += "{}\n".format(element.find('status').text)
	#responseView += "\n{}\n".format(element.find('synopsis').text)
	#responseView += "```"
	
	return embed

def format_manga(element):
	if element is None:
		return 'No Results Found! (You fucking normie...)'
	
	return 'https://myanimelist.net/manga/{}'.format(element.find('id').text)
	
	# for child in element:
		# for infoTag in child:
			# print('{}: {}'.format(infoTag.tag, infoTag.text))
		# print('------------------')