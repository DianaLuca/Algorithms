import urllib
from twurl import augment

# realDonaldTrump

print '* Calling Twitter...'
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
        {'screen_name': 'realDonaldTrump', 'count': '2'} )
print url
connection = urllib.urlopen(url)
data = connection.read()
print data
headers = connection.info().dict
# print headers


# Go to "http://jsonprettyprint.com/" and parse the response of "print data"