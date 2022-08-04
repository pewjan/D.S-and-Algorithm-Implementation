#sometimes chooses to pass sometimes chooses not to. sometimes it chooses to beat 50% of the people, sometimes chooses to time out 
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestValue = float("infinity")
        nums.sort()
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = nums[left] + nums[right] + nums[i]
                if threeSum == target:
                    return target
                if abs(threeSum - target) < abs(closestValue-target):
                    closestValue = threeSum
                if threeSum > target:
                    right-=1
                else:
                    left+=1

        return closestValue  
                
            
        
        
        
        
        
        
        
        
