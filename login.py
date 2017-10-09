import tweepy
from tweepy import OAuthHandler
consumer_key = '73vVAw72kSDIIwqO4ri0vPx3L'
consumer_secret = 'IL5uugcwQph0S45U4uKEdF5CEdKyhT280CNunqBCC6hgJZXjvf'
access_token = '915874251797798912-W0y8ACwMwP0AXso3dWTyeuGEt4Nhls8'
access_secret = 'qBXSV13msJR3yKtSWomXzCiRh9kMbB0Q1J3YGqcgo7D1V'
auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth,wait_on_rate_limit=True)


