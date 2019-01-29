import praw
import re
import time

reddit = praw.Reddit(client_id='IeKfR8JGHvtwOA',
				client_secret='lj9NDVC0tgMVcmbQUxXRPFFEb2M',
				user_agent='<console:reddit_bot:0.0.1 (by /u/python_bot_bjl)>', 
				username='python_bot_bjl',
				password='123456')
subreddits = ['funny', 'cats', 'mildlyinteresting']
pos = 0
errors = 0

title = "Funny Cat"
url = "https://imgur.com/r/funnycats/LOAi2kS"

def post():
	global subreddits
	global pos
	global errors
	try:
		subreddit = reddit.subreddit(subreddits[pos])
		subreddit.submit(title, url=url)
		print("Posted to " + subreddits[pos])
		pos = pos + 1

		if (pos <= len(subreddits) - 1):
			post()
		else:
			print ("Done")
	except praw.exceptions.APIException as e:
		if (e.error_type == "RATELIMIT"):
			delay = re.search("(\d+) minutes", e.message)

			if delay:
				delay_seconds = float(int(delay.group(1)) * 60)
				time.sleep(delay_seconds)
				post()
			else:
				delay = re.search("(\d+) seconds", e.message)
				delay_seconds = float(delay.group(1))
				time.sleep(delay_seconds)
				post()
	except:
		errors = errors + 1
		if (errors > 5):
			print("crashed")
post()
