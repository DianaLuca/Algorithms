# Scraping URL's from HTML using BeautifulSoup

import urllib.request
from bs4 import BeautifulSoup

# enter: http://www.dr-chuck.com
# url = input('Enter url - ')
url = 'http://www.dr-chuck.com'

# Read a html page
html = urllib.request.urlopen(url).read()
# print('html = {}'.format(html))

# Use BeautifulSoup to parse the html page
# soup = BeautifulSoup(html)
soup = BeautifulSoup(html, "html.parser")

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes
tags = soup('a')

for tag in tags:
    print('TAG: {}'.format(tag))
    print('URL: {}' .format(tag.get('href', None)))
    print('Contents: {}'.format(tag.contents[0]))
    print('Attrs: {}'.format(tag.attrs))