from Modules.MAL.LocalEntry import LocalEntry

def from_json_object(jsonObj):
	return LocalEntry(**(jsonObj))
	