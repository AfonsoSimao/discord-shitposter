
from discord import Embed
import sys

def format_anime(element):
	if element is None:
		return {"content": 'No Results Found! (You fucking normie...)'}

	try:
		embed = Embed(title=element.title, description=element.type, color=0x00ff00, url="https://myanimelist.net/anime/{}\n".format(element.mal_id))
		#embed.set_thumbnail(url=element.image)
		embed.set_image(url=element.image_url)
		if len(element.genres) > 0:
			embed.add_field(name="Genres", value=", ".join(["[{}]({})".format(g.name, g.url) for g in element.genres]), inline=False)
		if len(element.studios) > 0:
			embed.add_field(name="Studios", value=", ".join(["[{}]({})".format(g.name, g.url) for g in element.studios]), inline=False)
		embed.add_field(name="Status", value=element.status, inline=True)
		embed.add_field(name="Episodes", value=element.episodes, inline=True)
		embed.add_field(name="Score", value="{} (#{})".format(element.score, element.rank), inline=True)
		embed.add_field(name="Plot", value=(element.synopsis if len(element.synopsis) <= 1024 else "{}...".format(element.synopsis[0:1021])), inline=False)
		if(element.status == 'Currently Airing'):
			embed.add_field(name="Airs on", value=element.broadcast, inline=True)
		embed.add_field(name="List", value="[Add to my list](https://myanimelist.net/ownlist/anime/add?selected_series_id={})".format(element.mal_id), inline=True)

		## The 'related' property gets set to an empty list if it doesn't exist
		if not isinstance(element.related, list):
			for pName, pValue in element.related.items():
				embed.add_field(name=pName, value=", ".join(["[{}]({})".format(g.name, g.url) for g in pValue]), inline=False)

		embed.set_footer(text = "From {}".format(element.aired.string))
	except:
		print(sys.exc_info()[0])
		return None

	return {"embed": embed}

def format_manga(element):
	if element is None:
		return {"content": 'No Results Found! (You fucking normie...)'}

	embed = Embed(title=element.title, description=element.type, color=0x00ff00, url="https://myanimelist.net/manga/{}\n".format(element.mal_id))
	#embed.set_thumbnail(url=element.image)
	embed.set_image(url=element.image_url)
	if len(element.genres) > 0:
		embed.add_field(name="Genres", value=", ".join(["[{}]({})".format(g.name, g.url) for g in element.genres]), inline=False)
	if len(element.authors) > 0:
		embed.add_field(name="Authors", value=", ".join(["[{}]({})".format(g.name, g.url) for g in element.authors]), inline=False)
	embed.add_field(name="Volumes", value=element.volumes, inline=True)
	embed.add_field(name="Chapters", value=element.chapters, inline=True)
	embed.add_field(name="Status", value=element.status, inline=True)
	embed.add_field(name="Score", value="{} (#{})".format(element.score, element.rank), inline=True)
	embed.add_field(name="Plot", value=(element.synopsis if len(element.synopsis) <= 1024 else "{}...".format(element.synopsis[0:1021])), inline=False)
	
	#due to login problems, can't verify that this is the correct url for manga. Will uncomment once confirmed.
	#embed.add_field(name="List", value="[Add to my list](https://myanimelist.net/ownlist/manga/add?selected_series_id={})".format(element.mal_id), inline=True)

	if not isinstance(element.related, list):
		for pName, pValue in element.related.items():
			embed.add_field(name=pName, value=", ".join(["[{}]({})".format(g.name, g.url) for g in pValue if g.name]), inline=False)

	embed.set_footer(text = "From {}".format(element.published.string))



	return {"embed": embed}
