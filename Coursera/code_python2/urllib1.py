import urllib

fhand = urllib.urlopen('http://www.py4inf.com/code_python2/romeo.txt')
for line in fhand:
    print line.strip()

