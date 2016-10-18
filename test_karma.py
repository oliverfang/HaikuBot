import praw
import pprint
import operator

user_agent = "OSX:test_karma:v0.1 (by /u/schai)"
r = praw.Reddit(user_agent=user_agent)

# get user name
user_name = "schai"
user = r.get_redditor(user_name)

# limit # of items
thing_limit = 25

# get all posts in limit
posts = user.get_submitted(limit=thing_limit)

# get karma value from each post
post_karma = {}
for thing in posts:
	subreddit = thing.subreddit.display_name
	post_karma[subreddit] = (post_karma.get(subreddit, 0) + thing.score)

# sort and print
post_karma = sorted(post_karma.items(), key=operator.itemgetter(1))
pprint.pprint(post_karma)

# get all comments in limit
comments = user.get_comments(limit=thing_limit)

# get karma value from each comment
comment_karma = {}
for thing in comments:
	subreddit = thing.subreddit.display_name
	comment_karma[subreddit] = (comment_karma.get(subreddit, 0) + thing.score)

# sort and print
comment_karma = sorted(comment_karma.items(), key=operator.itemgetter(1))
pprint.pprint(comment_karma)
