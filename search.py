import login
import functs
import tweepy
import csv
itemCount=2
query=['isro']
csvfile="isro.csv"
jsonfile="isro.json"
#Search a Particular HashTag
for status in tweepy.Cursor(login.api.search,q=query).items(itemCount):
    print (status._json)
    functs.json_dump(status._json,jsonfile)
    functs.csv_dump(csvfile,status.id,status.created_at,status.text.encode('utf-8'))
    functs.mongo_dump(status._json,'isro')




