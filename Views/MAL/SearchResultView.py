import xml.etree.ElementTree as ET

def search_result(element):
	if element is None:
		return 'No Results Found! (You fucking normie...)'
	
	return 'https://myanimelist.net/anime/{}'.format(element.find('id').text)

	# for child in element:
		# for infoTag in child:
			# print('{}: {}'.format(infoTag.tag, infoTag.text))
		# print('------------------')