import sys

class LocalEntry:
	def __init__(self, **kwds):
		try:
			for k, v in kwds.items():
				if isinstance(v, dict):
					kwds[k] = LocalEntry(**v)
				elif isinstance(v, list):
					kwds[k] = [(LocalEntry(**i) if isinstance(i, dict) else i) for i in v]
			
			self.__dict__.update(kwds)
		except (NameError, TypeError, AttributeError) as e:
			print (e)
		except:
			print("LocalEntry_Init: {}".format(sys.exc_info()[0]))
	
	
	
	
		
		