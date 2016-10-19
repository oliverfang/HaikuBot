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
	msg = '%s\n\n %s\n\n %s' % (haiku[0], haiku[1], haiku[2])
	comment.reply(msg)
	print("Haiku found! Replied to comment.")

if __name__ == '__main__':
	# define user agent
	user_agent = "OSX:check_comment:v0.1 (by /u/schai)"
	r = praw.Reddit(user_agent=user_agent)
	r.login('the_haiku_poet', 'haiku_pass_word')
	r.set_oauth_app_info(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

	already_done = []

	# get subreddit
	subreddit = r.get_subreddit('bottest')

	# get the top 3 submissions
	limit = 3
	for submission in subreddit.get_hot(limit=limit):
		# get all comments
		comments = submission.comments
		for comment in comments:
			# handle exception when comment is empty
			try: 
				try: 
					# get comment text
					body = str(comment.body)
					haiku = isHaiku(str(comment.body))
					if haiku != False:
						# print the haiku
						bot_action(comment, haiku)
					else:
						print("Not a haiku")
				except UnicodeEncodeError:
					print("Unicode Error")
			except AttributeError:
				print("Comment not found.")

