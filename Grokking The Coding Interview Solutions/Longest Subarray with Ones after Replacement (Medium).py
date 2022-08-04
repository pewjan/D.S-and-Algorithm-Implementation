class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        windowDict = defaultdict(int)
        windowStart = 0
        longestFlip = 0
        maxCounter = 0
        
        
        for windowEnd in range(len(nums)):
            windowDict[nums[windowEnd]] +=1
            maxCounter = windowDict[1]
            
            
            while (windowEnd - windowStart + 1 - maxCounter > k):
                if windowDict[nums[windowStart]] == 1:
                    del windowDict[nums[windowStart]]
                else:
                    windowDict[nums[windowStart]]-=1
                windowStart+=1
            
            
            longestFlip = max(longestFlip, windowEnd - windowStart + 1)
        return longestFlip
        
