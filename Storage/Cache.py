
import sys
import datetime
from Modules.MAL.LocalEntry import LocalEntry
from tinydb import TinyDB, Query, where


class CacheEntry:
	def __init__(self, term, type, last_update, item):
		self.term = term
		self.type = type
		self.last_update = last_update
		self.data = item.__dict__

		
def _isCacheValid(date, daysOld):
	threshold = datetime.date.today() - datetime.timedelta(days=daysOld)
	return threshold < datetime.datetime.strptime(date, "%d/%m/%Y").date()
		
		
class Cache:
	def __init__(self, cachePath):
		self._storage = TinyDB(cachePath)
		
	def get(self, query, type, daysOld = 7):
		Entry = Query()
		
		try:
			res = self._storage.get((Entry.term == query) & (Entry.type == type) & (Entry.last_update.test(_isCacheValid, daysOld)))
		except (NameError, TypeError, AttributeError) as e:
			print (e)
			res = None
		except:
			print(sys.exc_info()[0])
			res = None
		
		return LocalEntry(**(res['data'])) if res is not None else res
		
	def exists(self, query, type):
		Entry = Query()
		return self._storage.get((Entry.term == query) & (Entry.type == type)) is not None
		
		
	def add(self, query, element, type):
		Entry = Query()
		
		item = CacheEntry(query, type, datetime.datetime.strftime(datetime.date.today(), "%d/%m/%Y"), element)
				
		try:
			if self.exists(query, type):
				self._storage.update(item.__dict__, (Entry.term == query) & (Entry.type == type))
			else:
				self._storage.insert(item.__dict__)
		except (NameError, TypeError, AttributeError) as e:
			print ("Cache_Add: {}".format(e))
			res = None
		except:
			print("Cache_Add: {}".format(sys.exc_info()[0]))
			res = None
				
				
				
		
		
		
		
		
		
		