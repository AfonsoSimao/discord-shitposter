import datetime
import json
from tinydb import TinyDB, Query
from tinydb.operations import add


class PollBuilder:
	POLL_NOT_FOUND = 1
	POLL_CLOSED = 2
	NOT_OP = 3
	MULTIPLE_VOTE = 4
	
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
		return self._pollStorage.insert({'poll': pollText, 'state': 'open', 'yes': [], 'no':[], 'created_on': datetime.datetime.strftime(datetime.date.today(), "%d/%m/%Y"), 'created_by': creator })
		
	def add_vote(self, user, choice, pollid):
		
		poll = self.get_poll(pollid)
		
		if poll is None:
			return PollBuilder.POLL_NOT_FOUND
			
		if poll['state'] == 'closed':
			return PollBuilder.POLL_CLOSED
		
		if user not in poll['yes'] and user not in poll['no']:
			self._pollStorage.update(add(choice, [user]), doc_ids=[pollid])
			print('{} votes {}!'.format(user, choice))
			return 0
			
		return PollBuilder.MULTIPLE_VOTE
		
	def close_poll(self, pollid, op):
		poll = self.get_poll(pollid)
		
		if poll is None:
			return PollBuilder.POLL_NOT_FOUND
		if poll['state'] == 'closed':
			return PollBuilder.POLL_CLOSED
		if poll['created_by'] != op:
			return PollBuilder.NOT_OP
		
		self._pollStorage.update({'state': 'closed'}, doc_ids=[pollid])
		print('Poll\'s Closed! {}'.format(pollid))
		return poll
		
		
		
		
		
		
		
		