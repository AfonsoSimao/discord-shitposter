import datetime
import json
from tinydb import TinyDB, Query
from tinydb.operations import add


class PollBuilder:
	def __init__(self):
		self._pollStorage = TinyDB('Storage/TinyDB/polls.json')

	def get_poll(self, id):
		return self._pollStorage.get(doc_id=id)
		
	def list_open_polls(self):
		Poll = Query()
		return self._pollStorage.search(Poll.state == 'open')
		
	def add_poll(self, pollText, creator):
		Poll = Query()
		print("New poll: {}".format(pollText))
		self._pollStorage.insert({'poll': pollText, 'state': 'open', 'yes': [], 'no':[], 'created_on': datetime.datetime.strftime(datetime.date.today(), "%d/%m/%Y"), 'created_by': creator })
		
	def add_vote(self, user, choice, pollid):
		print('{} votes {}!'.format(user, choice))
		poll = _self.get_poll(pollid)
		self._pollStorage.update(add(choice, [user]), doc_ids=[pollid])
	
	def close_poll(self, pollid):
		self._pollStorage.update({'state': 'closed'}, doc_ids=[pollid])
		print('Poll\'s Closed! {}'.format(pollid))