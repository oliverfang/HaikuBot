import praw
import pprint

# define user agent
user_agent = "OSX:check_comment:v0.1 (by /u/schai)"
r = praw.Reddit(user_agent=user_agent)
r.login()

user_name = 'schai'

already_done = []

# get subreddit
subreddit = r.get_subreddit('lego')

# define keywords
keywords = ['minifig']

# get the top 3 submissions
limit = 3
for submission in subreddit.get_hot(limit=limit):
	# get all comments
	comments = submission.comments
	for comment in comments:
		# handle exception when comment is empty
		try: 
			# get comment text
			body = comment.body
			# check if comment has any of the keywords
			has_keyword = any(string in body for string in keywords)
			# check commentID
			if comment.id not in already_done and has_keyword:
				# send a message
				msg = '[PRAW related thread](%s)' % submission.short_link
				r.send_message(user_name, 'PRAW Thread', msg)
				print("Sent message to %s" % user_name)
				# add comment ID to list of done comments
				#already_done.add(comment.id) 
		except AttributeError:
			print("Comment not found.")
