class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowStart = 0
        windowDict = defaultdict(int)
        longest = 0 
        biggestCount = 0
        
        for windowEnd in range(len(s)):
            windowDict[s[windowEnd]] +=1
            biggestCount = max(biggestCount, windowDict[s[windowEnd]])
            
            while (windowEnd - windowStart + 1 - biggestCount > k):
                if windowDict[s[windowStart]] == 1:
                    del windowDict[s[windowStart]]
                else:
                    windowDict[s[windowStart]]-=1
                windowStart+=1
            
            longest = max(longest, windowEnd - windowStart + 1)
        return longest
                
        
        
