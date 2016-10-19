import praw
import pprint
import os
import sys
sys.path.append(os.getcwd())
from isHaiku import isHaiku

CLIENT_ID = 'D2gIAqWhCFn8Cw'
CLIENT_SECRET = 'pUFeCsnvQ_VIxZPC_9IRWh33gyA'
REDIRECT_URI = 'http://127.0.0.1:65010/authorize_callback'

def bot_action(comment, haiku):
	# reply to comment with haiku in proper formatting
	msg = '%s\n\n %s\n\n %s' % (haiku[0], haiku[1], haiku[2])
	comment.reply(msg)
	print("Haiku found! Replied to comment.")

if __name__ == '__main__':
	# define user agent
	user_agent = "OSX:haiku_checker:v0.1 (by /u/the_haiku_poet)"
	r = praw.Reddit(user_agent=user_agent)
	r.set_oauth_app_info(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

	# look at all incoming comments
	for comment in praw.helpers.comment_stream(r, 'bottest'):
		try: # handle unicode errors
			# get comment text
			body = str(comment.body)
			haiku = isHaiku(str(comment.body))
			if haiku != False:
				# if haiku found, take action
				bot_action(comment, haiku)
			else:
				print("Not a haiku")
		except UnicodeEncodeError:
			print("Unicode Error")