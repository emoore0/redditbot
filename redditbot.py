#!/usr/bin/python
import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')
#Reddit object is created

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt",'r') as f:
        # with opens the files for us, will close it, and all handle any errors. 
        #'r' means read
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split('\n')
        #splits when there is a new line and creates a list
        posts_replied_to = list(filter(None, posts_replied_to))
        #removes any None values

subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search('I love Python',submission.title,re.IGNORECASE):
            #this uses regular expressions and be case insensitive
            submission.reply("The King of all bots says: I like Java better :p")
            print('Bot replying to: ',submission.title,'by',submission.author)
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")