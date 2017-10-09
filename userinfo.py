import tweepy
import login
import functs

user=login.api.me()

print user.name
print user.screen_name
print user.id
print user.created_at
for status in tweepy.Cursor(login.api.home_timeline).items(1):
    print (status.text)
    functs.json_print(status._json)
