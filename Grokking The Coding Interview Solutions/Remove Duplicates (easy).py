class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0,1,0,1,1,2,2,3,3,4]
        left = 1
        right = 1
        while right < len(nums):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left+=1
            right+=1
        return left
            
                
    
        
