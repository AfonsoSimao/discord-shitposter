
import sys
from tinydb import TinyDB, Query, where
from tinydb.operations import add


class KeyValueStorage:
	def __init__(self, path, allowMulti = False):
		self._storage = TinyDB(path)
		self.allowMulti = allowMulti

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

	def exists(self, key):
		Entry = Query()
		return self._storage.get(Entry.key == key) is not None

	def add_value(self, key, value):
		Entry = Query()

		try:
			if self.exists(key):
				if not self.allowMulti:
					self._storage.update({"key":key,"value":[value]}, Entry.key == key)
				else:
					self._storage.update(add("value", [value]), Entry.key == key)
			else:
				self._storage.insert({"key":key,"value":[value]})
		except (NameError, TypeError, AttributeError) as e:
			print ("KeyValue_Add: {}".format(e))
		except:
			print("KeyValue_Add: {}".format(sys.exc_info()[0]))
