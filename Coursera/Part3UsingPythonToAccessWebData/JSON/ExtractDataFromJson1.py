# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and
#  extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and
# the other is the actual data you need to process for the assignment.
#
# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_369923.json (Sum ends with 79)


import urllib.request
import urllib.parse
import json

# enter: " http://python-data.dr-chuck.net/comments_369923.json "
url = input("Enter url ~ ")

uh = urllib.request.urlopen(url)
data = uh.read()

# print(type(data)) #'bytes'

try:
    info = json.loads(data.decode("utf-8"))
except:
    info = None

# print(json.dumps(info, indent = 4)) #print the formatted info 'dict'

# simpler_sum = 0
# for comment in info['comments']:
#     simpler_sum += comment['count']

simpler_sum = sum(comment['count'] for comment in info['comments'])
print(simpler_sum)