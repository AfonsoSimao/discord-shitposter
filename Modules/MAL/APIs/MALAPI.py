
import requests
import Modules.MAL.Mappers.MALtoLocalMapper as MALMapper

ANIME_SEARCH_URL = "https://myanimelist.net/api/anime/search.xml?q={}"
MANGA_SEARCH_URL = "https://myanimelist.net/api/manga/search.xml?q={}"

class MALAPI:

	def __init__(self, user, pwd):
		self._user = user
		self._pwd = pwd		
		
	def get_anime(self, query):
		return self._get(query, ANIME_SEARCH_URL)
		
	def get_manga(self, query):
		return self._get(query, MANGA_SEARCH_URL)
		
	def _get(self, query, apiUrl):
		query = query.lower()
		
		resp = requests.get(apiUrl.format(query.replace(' ', '+')), auth=(self._user, self._pwd))
	
		print(apiUrl.format(query.replace(' ', '+')) + " : {}".format(resp.status_code))
	
		if(resp.status_code == 204):
			return None
	
		return MALMapper.from_xml_string(resp.text)