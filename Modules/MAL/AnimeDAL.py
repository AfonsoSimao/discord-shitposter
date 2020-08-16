
import Configs.MyCreds as MyCreds
import sys
import asyncio
import json

from Storage.Cache import Cache
from Modules.MAL.APIs.MALAPI import MALAPI
from Modules.MAL.APIs.JikanAPI import JikanAPI



class AnimeDAL:
	def __init__(self):
		self.__cache = Cache('Storage/TinyDB/localMAL.json')
		#self.__malAPI = MALAPI(MyCreds.MALUser, MyCreds.MALPassword)
		self.__jikanAPI = JikanAPI()

	async def get_anime(self, query):
		return await self.__check_cache(query, "anime", AnimeDAL.__compose_anime)
		
	async def get_manga(self, query):
		return await self.__check_cache(query, "manga", AnimeDAL.__compose_manga)
		
		
	async def __check_cache(self, query, type, entrySupplier):
		query = query.lower()
		
		item = self.__cache.get(query, type)
		
		if item is None:
			item = await entrySupplier(self, query)
			
			if item is not None:
				self.__cache.add(query, item, type)
		
		return item
		
	async def __compose_anime(self, query):
		#item = self.__malAPI.get_anime(query)
		try:
			return await self.__jikanAPI.search_anime(query)
			
		except (NameError, TypeError, AttributeError) as e:
			print (e)
			item = None
		except:
			print(sys.exc_info()[0])
			item = None
		
		
		return item
		
	async def __compose_manga(self, query):
		#item = self.__malAPI.get_manga(query)
		try:
			return await self.__jikanAPI.search_manga(query)
			
		except (NameError, TypeError, AttributeError) as e:
			print (e)
			item = None
		except:
			print(sys.exc_info()[0])
			item = None
		
		
		return item
		
		
		
		
		
		
		
		
		
		
		
		
		
		