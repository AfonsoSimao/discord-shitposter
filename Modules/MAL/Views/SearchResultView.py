
from discord import Embed

def format_anime(element):
	if element is None:
		return {"content": 'No Results Found! (You fucking normie...)'}
	
	desc = element.english if element.english is not None else ''
	
	embed = Embed(title=element.title, description=desc, color=0x00ff00, url="https://myanimelist.net/anime/{}\n".format(element.id))
	embed.set_thumbnail(url=element.image)
	#embed.set_image(url="https://myanimelist.cdn-dena.com/images/anime/2/75259.jpg")
	embed.add_field(name="Type", value=element.type, inline=True)
	embed.add_field(name="Status", value=element.status, inline=True)
	embed.add_field(name="Episodes", value=element.episodes, inline=True)
	embed.add_field(name="Score", value=element.score, inline=True)
	
	embed.set_footer(text = element.synopsis)
	
	
	
	return {"embed": embed}

def format_manga(element):
	if element is None:
		return {"content": 'No Results Found! (You fucking normie...)'}
	
	return {"content": 'https://myanimelist.net/manga/{}'.format(element.id)}
