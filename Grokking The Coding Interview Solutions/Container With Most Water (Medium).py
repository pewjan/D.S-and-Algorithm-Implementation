class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1 
        maxWater = 0
        while left < right:
            maxWater = max(maxWater, (right - left) * min(height[left], height[right]))
            if height[right] > height[left]:
                left+=1

            elif height[right] <= height[left]:
                right-=1
        return maxWater
            
