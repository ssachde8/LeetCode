class Solution(object):
    def groupAnagrams(self, s_list):
        """
        :type s_list: List[str]
        :rtype: List[List[str]]
        """
        
        lookup = {}
        
        for word in s_list:
            
            sorted_word = "".join(sorted(word))
            
            if sorted_word in lookup:
                lookup[sorted_word] += [word] 
            else:
                lookup[sorted_word] = [word]
                
        result = []
        for word in lookup:
            result.append(lookup[word])
            
        return result