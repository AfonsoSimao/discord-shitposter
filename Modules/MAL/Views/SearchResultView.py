
from discord import Embed

def format_anime(element):
	if element is None:
		return {"content": 'No Results Found! (You fucking normie...)'}
	
	desc = element.english if element.english is not None else ''
	
	embed = Embed(title=element.title, description=element.type, color=0x00ff00, url="https://myanimelist.net/anime/{}\n".format(element.id))
	#embed.set_thumbnail(url=element.image)
	embed.set_image(url=element.image)
	embed.add_field(name="Status", value=element.status, inline=True)
	embed.add_field(name="Episodes", value=element.episodes, inline=True)
	embed.add_field(name="Score", value=element.score, inline=True)
	embed.add_field(name="Plot", value=element.synopsis, inline=False)
	
	embed.set_footer(text = "From {} to {}".format(element.start_date, element.end_date if element.end_date is not None else "\u2014"))
	
	
	
	return {"embed": embed}

def format_manga(element):
	if element is None:
		return {"content": 'No Results Found! (You fucking normie...)'}
	
	return {"content": 'https://myanimelist.net/manga/{}'.format(element.id)}
