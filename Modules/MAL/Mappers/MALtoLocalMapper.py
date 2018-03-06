
import html
import xml.etree.ElementTree as ET

class Local:
	def __init__(self):
		pass
		
	def __str__(self):
		return self.__dict__.__str__()
		

def from_xml_string(xml_string):
	item = ET.fromstring(xml_string)[0]
	parsed = Local()
	
	for child in item:
		setattr(parsed, child.tag, child.text)
	
	parsed.synopsis = html.unescape(html.unescape(parsed.synopsis)).replace('<br />', '\n')
		
	return parsed