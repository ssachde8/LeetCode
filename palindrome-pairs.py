class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        lookup = {word:i for i,word in enumerate(words)}
        res = []
        
        for i, w in enumerate(words): # w-> word
            for j in range(0, len(w)+1):
                a = w[:j] # a is prefix
                b = w[j:] # b is suffix
                
                if a == a[::-1]:
                    if lookup.has_key(b[::-1]) and lookup[b[::-1]] != i:
                        res.append( ( lookup[b[::-1]], i ))
                        
                if b == b[::-1]:
                    if lookup.has_key(a[::-1]) and lookup[a[::-1]] != i:
                        res.append( ( i, lookup[a[::-1]]))
                        
        return list(set(res))