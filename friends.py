import login
import functs
import tweepy
import csv
itemCount=1
count=0
#Find followers count of specific user
user=login.api.get_user('isro')
print user.followers_count
#find list of followers
for follower in login.api.followers_ids('isro'):
    print login.api.get_user(follower).screen_name