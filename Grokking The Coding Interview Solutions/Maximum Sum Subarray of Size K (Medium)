class Solution(object):
    def minSubArrayLen(self, target, nums):
        lengthMin = float("infinity")
        windowStart = 0
        windowSum = 0        
        
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
        
            while windowSum >= target:
                lengthMin = min(lengthMin, windowEnd - windowStart + 1)
                windowSum-=nums[windowStart]
                windowStart+=1
        return 0 if lengthMin == float("infinity") else lengthMin
