
import sys
from tinydb import TinyDB, Query, where

		
class KeyValueStorage:
	def __init__(self, path):
		self._storage = TinyDB(path)
		
	def get(self, key):
		Entry = Query()
		
		try:
			res = self._storage.get(Entry.key == key)
		except (NameError, TypeError, AttributeError) as e:
			print (e)
			res = None
		except:
			print(sys.exc_info()[0])
			res = None
		
		return res["value"] if res is not None else None
		
	def exists(self, query, type):
		Entry = Query()
		return self._storage.get((Entry.key == key) is not None
		
	def add(self, key, value):
		Entry = Query()
		
		item = CacheEntry(query, type, datetime.datetime.strftime(datetime.date.today(), "%d/%m/%Y"), element)
				
		try:
			if self.exists(key):
				self._storage.update({key:value}, Entry.key == key)
			else:
				self._storage.insert({key:value})
		except (NameError, TypeError, AttributeError) as e:
			print ("Cache_Add: {}".format(e))
			res = None
		except:
			print("Cache_Add: {}".format(sys.exc_info()[0]))
			res = None
				
				
				
		
		