class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        windowDict = defaultdict(int)
        windowStart = 0
        longest = 0
        
        for windowEnd in range(len(s)):

            while s[windowEnd] in windowDict:
                if windowDict[s[windowStart]] == 1:
                    del windowDict[s[windowStart]]
                else:
                    windowDict[s[windowStart]]-=1
                windowStart+=1

            windowDict[s[windowEnd]]+=1
            
            longest = max(longest, windowEnd - windowStart + 1)
        
        return longest
            
    
        
        
        
        
