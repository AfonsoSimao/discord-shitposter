
from discord import Embed

def format_anime(element):
	if element is None:
		return {"content": 'No Results Found! (You fucking normie...)'}

	try:
		desc = element.english if element.english is not None else ''

		embed = Embed(title=element.title, description=element.type, color=0x00ff00, url="https://myanimelist.net/anime/{}\n".format(element.id))
		#embed.set_thumbnail(url=element.image)
		embed.set_image(url=element.image)
		if len(element.genre) > 0:
			embed.add_field(name="Genres", value=", ".join(["[{}]({})".format(g.name, g.url) for g in element.genre]), inline=False)
		if len(element.studio) > 0:
			embed.add_field(name="Studios", value=", ".join(["[{}]({})".format(g.name, g.url) for g in element.studio]), inline=False)
		embed.add_field(name="Status", value=element.status, inline=True)
		embed.add_field(name="Episodes", value=element.episodes, inline=True)
		embed.add_field(name="Score", value="{} (#{})".format(element.score, element.rank), inline=True)
		embed.add_field(name="Plot", value=(element.synopsis if len(element.synopsis) <= 1024 else "{}...".format(element.synopsis[0:1021])), inline=False)
		if(element.status == 'Currently Airing'):
			embed.add_field(name="Airs on", value=element.broadcast, inline=False)

		## The 'related' property gets set to an empty list if it doesn't exist
		if not isinstance(element.related, list):
			for pName, pValue in element.related.__dict__.items():
				embed.add_field(name=pName, value=", ".join(["[{}]({})".format(g.title, g.url) for g in pValue]), inline=False)

		embed.set_footer(text = "From {}".format(element.aired_string))
	except:
		print(sys.exc_info()[0])
		return None

	return {"embed": embed}

def format_manga(element):
	if element is None:
		return {"content": 'No Results Found! (You fucking normie...)'}

	desc = element.english if element.english is not None else ''

	embed = Embed(title=element.title, description=element.type, color=0x00ff00, url="https://myanimelist.net/manga/{}\n".format(element.id))
	#embed.set_thumbnail(url=element.image)
	embed.set_image(url=element.image)
	embed.add_field(name="Genres", value=", ".join(["[{}]({})".format(g.name, g.url) for g in element.genre]), inline=False)
	embed.add_field(name="Authors", value=", ".join(["[{}]({})".format(g.name, g.url) for g in element.author]), inline=False)
	embed.add_field(name="Volumes", value=element.volumes, inline=True)
	embed.add_field(name="Chapters", value=element.chapters, inline=True)
	embed.add_field(name="Status", value=element.status, inline=True)
	embed.add_field(name="Score", value="{} (#{})".format(element.score, element.rank), inline=True)
	embed.add_field(name="Plot", value=(element.synopsis if len(element.synopsis) <= 1024 else "{}...".format(element.synopsis[0:1021])), inline=False)

	if not isinstance(element.related, list):
		for pName, pValue in element.related.__dict__.items():
			embed.add_field(name=pName, value=", ".join(["[{}]({})".format(g.title, g.url) for g in pValue]), inline=False)

	embed.set_footer(text = "From {}".format(element.published_string))



	return {"embed": embed}
