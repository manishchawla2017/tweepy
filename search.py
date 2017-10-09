import login
import functs
import tweepy
import csv
itemCount=20
query=['isro']
for status in tweepy.Cursor(login.api.search,q=query).items(itemCount):
        print (status._json)
        functs.json_dump(status._json,'isro.json')
        functs.csv_dump('isro.csv',status.id,status.created_at,status.text.encode('utf-8'))
        functs.mongo_dump(status._json)



