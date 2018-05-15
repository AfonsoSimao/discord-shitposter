
import json
import requests
import Modules.MAL.Mappers.MALtoLocalMapper as MALMapper
import Modules.MAL.Mappers.JikantoLocalMapper as JikanMapper

ANIME_SEARCH_URL = "https://api.jikan.moe/anime/{}"
MANGA_SEARCH_URL = "https://api.jikan.moe/manga/{}"

class JikanAPI:

	def __init__(self):
		pass
		
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