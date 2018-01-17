from random import *
from string import *


# solution 1
class Codec:

    alphabet = ascii_letters + "0123456789"

    def __init__(self):
        self.tiny2url = {}
        self.url2tiny = {}

    def encode(self, url):
        if url not in self.url2tiny:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.tiny2url:
                self.tiny2url[code] = url
                self.url2tiny[url] = code
        return 'http://tinyurl.com/' + self.url2tiny[url]

    def decode(self, tiny):
        return self.tiny2url[tiny[-6:]]


# solution 2
class CodecT:

    def __init__(self):
        self.hashmaq = {}

    def encode(self, longUrl):
        tiny = hash(longUrl)
        self.hashmaq[tiny] = longUrl
        return tiny

    def decode(self, shortUrl):
        print(self.hashmaq)
        return self.hashmaq[shortUrl]


def main():
    c = CodecT()
    print(c.decode(c.encode("https://leetcode.com/problems/design-tinyurl")))

if __name__ == "__main__":
    main()
