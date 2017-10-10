import json
import csv
import sys
from pymongo import MongoClient
def json_print(tweet):
    print (json.dumps(tweet))
def json_dump(tweet,outfile):
    with open(outfile,'w') as jsonfile:
            json.dump(tweet, jsonfile)
def csv_dump(outfile,id, created_at,text):
    file = open(outfile, 'a')
    writer = csv.writer(file)
    writer.writerow(["id", "created_at", "text"])
    writer.writerow([id, created_at, text])
    file.close()
def mongo_dump(outfile,collections):
    MONGO_HOST='mongodb://localhost/twitterdb'
    client=MongoClient(MONGO_HOST)
    db=client.twitterdb
    db.collections.insert(outfile)


