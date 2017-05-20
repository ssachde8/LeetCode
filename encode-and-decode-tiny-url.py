class Codec:
    mp = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        genUrl = hash(longUrl)
        self.mp[genUrl] = longUrl
        return 'http://tinyurl.com/' + str(genUrl)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        genUrl = long(shortUrl.split('/')[-1])
        return self.mp[genUrl]
        
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))