class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])-1,-1,-1):
            prefix = strs[0][:i+1]
            validPrefix = True
            for j in range(1,len(strs)):
                if len(strs[j])<=i or strs[j][:i+1]!=prefix:
                    validPrefix = False
                    break
            if validPrefix:
                return prefix
        return ""