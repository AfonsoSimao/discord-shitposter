
import Configs.MyCreds as MyCreds

from Storage.Cache import Cache
from Modules.MAL.APIs.MALAPI import MALAPI
from Modules.MAL.APIs.JikanAPI import JikanAPI



class AnimeDAL:
	def __init__(self):
		self._cache = Cache('Storage/TinyDB/localMAL.json')
		self._malAPI = MALAPI(MyCreds.MALUser, MyCreds.MALPassword)
		self._jikanAPI = JikanAPI()

	def get_anime(self, query):
		return self._check_cache(query, "anime", AnimeDAL._compose_anime)
		
	def get_manga(self, query):
		return self._check_cache(query, "manga", AnimeDAL._compose_manga)
		
		
	def _check_cache(self, query, type, entrySupplier):
		query = query.lower()
		
		item = self._cache.get(query, type)
		
		if item is None:
			item = entrySupplier(self, query)
			
			if item is not None:
				self._cache.add(query, item, type)
		
		return item
		
	def _compose_anime(self, query):
		item = self._malAPI.get_anime(query)
		itemj = self._jikanAPI.get_anime(item.id)
		
		try:
			
			item.source = itemj.source
			item.aired_string = itemj.aired_string
			item.duration = itemj.duration
			item.rating = itemj.rating
			item.rank = itemj.rank
			item.broadcast = itemj.broadcast
			item.related = itemj.related
			item.studio = itemj.studio
			item.genre = itemj.genre
			item.opening_themes = itemj.opening_theme
			item.ending_themes = itemj.ending_theme
			
		except (NameError, TypeError, AttributeError) as e:
			print (e)
			item = None
		except:
			print(sys.exc_info()[0])
			item = None
		
		
		return item
		
	def _compose_manga(self, query):
		return self._malAPI.get_manga(query)