import collections
class Solution:

    def longestKSubstr(self, s, k):
        windowStart = 0
        windowDict = collections.defaultdict(int)
        longest = -1
        
        
        for windowEnd in range(len(s)):
            windowDict[s[windowEnd]]+=1
        
            
            while len(windowDict.keys()) > k:
                if windowDict[s[windowStart]] == 1:
                    del windowDict[s[windowStart]]
                else:
                    windowDict[s[windowStart]]-=1
                windowStart+=1
            if len(windowDict.keys()) == k:
                longest = max(longest, windowEnd - windowStart + 1)
            
        return longest
