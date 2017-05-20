class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = collections.defaultdict(int)
        candidates = set()
        for i, c in enumerate(s):
            # print(candidates, lookup)
            if c in lookup:
                candidates.discard(lookup[c])
            else:
                lookup[c] = i   # add char index to lookup
                candidates.add(i) # possible answer
            
        return min(candidates) if candidates else -1