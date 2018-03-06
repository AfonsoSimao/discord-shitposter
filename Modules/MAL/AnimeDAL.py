
import Configs.MyCreds as MyCreds

from Storage.Cache import Cache
from Modules.MAL.APIs.MALAPI import MALAPI


class AnimeDAL:
	def __init__(self):
		self._cache = Cache('Storage/TinyDB/localMAL.json')
		self._malAPI = MALAPI(MyCreds.MALUser, MyCreds.MALPassword)

	def get_anime(self, query):
		return self._check_cache(query, "anime", MALAPI.get_anime)
		
	def get_manga(self, query):
		return self._check_cache(query, "manga", MALAPI.get_manga)
		
		
	def _check_cache(self, query, type, entrySupplier):
		query = query.lower()
		
		item = self._cache.get(query, type)
		
		if item is None:
			item = entrySupplier(self._malAPI, query)
			
			##item manipulation goes here
			if item is not None:
				self._cache.add(query, item, type)
		
		return item
		
	