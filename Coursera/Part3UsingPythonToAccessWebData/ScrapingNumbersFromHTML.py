# Scraping Numbers from HTML using BeautifulSoup

# Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum = 2553)
# Actual data: http://python-data.dr-chuck.net/comments_369922.html (Sum ends with 21)

# Data Format
# The file is a table of names and comment counts.
# You can ignore most of the data in the file except for lines like the following:

# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
# <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
# <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

# You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.


import urllib.request
from bs4 import BeautifulSoup

# enter: actual data (test with sample data sum = 2553)
# url = input('Enter url - ')
# url = 'http://python-data.dr-chuck.net/comments_42.html'
url = 'http://python-data.dr-chuck.net/comments_369922.html'

# Read a html page
html = urllib.request.urlopen(url).read()
# print(' ---------- html = {}'.format(html))

# Use BeautifulSoup to parse the html page
# soup = BeautifulSoup(html)
soup = BeautifulSoup(html, "html.parser")

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes
tags = soup('span')

totalComments = 0
for tag in tags:
    print('TAG: {}'.format(tag))
    print('Comments: {}'.format(tag.contents[0]))
    totalComments += int(tag.contents[0])

print(totalComments)

simpler_sum = sum([int(tag.contents[0]) for tag in soup('span')])
