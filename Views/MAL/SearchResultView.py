import xml.etree.ElementTree as ET

def format_anime(element):
	if element is None:
		return 'No Results Found! (You fucking normie...)'
	
	return 'https://myanimelist.net/anime/{}'.format(element.find('id').text)

def format_manga(element):
	if element is None:
		return 'No Results Found! (You fucking normie...)'
	
	return 'https://myanimelist.net/manga/{}'.format(element.find('id').text)
	
	# for child in element:
		# for infoTag in child:
			# print('{}: {}'.format(infoTag.tag, infoTag.text))
		# print('------------------')