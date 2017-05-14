import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

# Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_369919.xml (Sum ends with 84)

while True:
    url = input('Enter location: ')
    if len(url) < 1:
        break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)

    comments = tree.findall('comments')

    print('Count:', len(comments[0]))
    S = sum([int(comment.find('count').text) for comment in comments[0]])
    print('Sum:', S)
