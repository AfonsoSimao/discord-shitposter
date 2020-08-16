import asyncio
import json
import requests
from jikanpy import AioJikan
import Modules.MAL.Mappers.JikantoLocalMapper as JikanMapper

ANIME_SEARCH_URL = "https://api.jikan.moe/anime/{}"
MANGA_SEARCH_URL = "https://api.jikan.moe/manga/{}"

class JikanAPI:

	def __init__(self):
		pass
		
	async def search_anime(self, query):
		async with AioJikan() as api:
			a = await api.search("anime", query, parameters={"limit": 5})
			if (a['results'][0]["title"].lower() == query):
				a = await api.anime(a['results'][0]["mal_id"])
			else:
				a = await api.anime(a['results'][0]["mal_id"]) #TODO: if no exact match was found we need to show a list to the user

		return JikanMapper.from_json_object(a) #TODO: if no exact match was found we need to show a list to the user

	async def search_manga(self, query):
		async with AioJikan() as api:
			a = await api.search("manga", query, parameters={"limit": 5})
			if (a['results'][0]["title"].lower() == query):
				a = await api.manga(a['results'][0]["mal_id"])
			else:
				a = await api.manga(a['results'][0]["mal_id"]) #TODO: if no exact match was found we need to show a list to the user

		return JikanMapper.from_json_object(a) #TODO: if no exact match was found we need to show a list to the user
		

	def get_anime(self, mal_id):

		return self._get(mal_id, ANIME_SEARCH_URL)
		
	def get_manga(self, mal_id):
		return self._get(mal_id, MANGA_SEARCH_URL)
		
	def _get(self, mal_id, apiUrl):
		
		resp = requests.get(apiUrl.format(mal_id))
	
		print(apiUrl.format(mal_id) + " : {}".format(resp.status_code))
	
		if(resp.status_code == 204):
			return None
	
		return JikanMapper.from_json_object(resp.json())