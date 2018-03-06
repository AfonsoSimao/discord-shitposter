import requests
import datetime
import Configs.MyCreds as MyVreds
import json
import xml.etree.ElementTree as ET
from tinydb import TinyDB, Query, where

ANIME_SEARCH_URL = "https://myanimelist.net/api/anime/search.xml?q={}"
MANGA_SEARCH_URL = "https://myanimelist.net/api/manga/search.xml?q={}"

def _isCacheOutdated(date):
	threshold = datetime.date.today() - datetime.timedelta(days=5)
	
	return datetime.datetime.strptime(date, "%d/%m/%Y") < threshold

class MALSearchAPI:
	def __init__(self, user, pwd):
		self._user = user
		self._pwd = pwd
		self._storage = TinyDB('Storage/TinyDB/localMAL.json')

	
		
	def _check_local(self, query, type):
		Anime = Query()
		known_results = self._storage.search((Anime.term == query) & (Anime.type == type)) # and not Anime.last_update.test(_isCacheOutdated)
		
		if len(known_results) > 0:
			return known_results[0]
			
		return None
		
	def _get_local(self, query):
		Anime = Query()
		known_results = self._storage.search(Anime.term == query)
		
		if len(known_results) > 0:
			return known_results[0]
			
		return None
		
	def _add_local(self, query, element, type):
		Anime = Query()
		
		print(ET.tostring(element, encoding='unicode', method='xml'))
		
		if self._check_local(query, type) is not None:
			self._storage.update({'data': elment}, (Anime.term == query) & (Anime.type == type))
		else:
			self._storage.insert({'term': query, 'type': type, 'data': ET.tostring(element, encoding='unicode', method='xml'), 'last_update': datetime.datetime.strftime(datetime.date.today(), "%d/%m/%Y") })
		
	def search_anime(self, query):
		return self.search_term(query, ANIME_SEARCH_URL, "anime")
		
	def search_manga(self, query):
		return self.search_term(query, MANGA_SEARCH_URL, "manga")
		
	def search_term(self, query, apiUrl, type):
		query = query.lower()
		
		print(datetime.datetime.strftime(datetime.date.today(), "%d/%m/%Y"))
		item = self._check_local(query, type)
		
		if item is None:
			resp = requests.get(apiUrl.format(query.replace(' ', '+')), auth=(self._user, self._pwd))
		
			print(apiUrl.format(query.replace(' ', '+')) + " : {}".format(resp.status_code))
		
			if(resp.status_code == 204):
				return None
		
			tree = ET.ElementTree(ET.fromstring(resp.text))
			item = tree.getroot()[0]
			
			self._add_local(query, item, type)
		else:
			
			item = ET.fromstring(item['data'])
			
		return item
			
			# for child in root:
				# for infoTag in child:
					# print('{}: {}'.format(infoTag.tag, infoTag.text))
				# print('------------------')
		
		
		
		
		
		
		
		