import sys
import json

class LocalEntry(dict):
	def __init__(self, **kwds):
		try:
			for k, v in kwds.items():
				if isinstance(v, dict):
					kwds[k] = LocalEntry(**v)
				elif isinstance(v, list):
					kwds[k] = [(LocalEntry(**i) if isinstance(i, dict) else i) for i in v]
			
			self.__dict__.update(kwds)
			dict.__init__(self, **self.__dict__)
		except (NameError, TypeError, AttributeError) as e:
			print (e)
		except:
			print("LocalEntry_Init: {}".format(sys.exc_info()[0]))

	def __str__(self):
		return self.__dict__.__str__()
	
	
	
		
		