class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        left = 0
        right = len(nums)-1
        end = len(nums)-1
        
        while left <= right:
            leftVal = nums[left] * nums[left]
            rightVal = nums[right] * nums[right]
            if leftVal > rightVal:
                output[end] = leftVal
                left+=1
            else:
                output[end] = rightVal
                right-=1
            end-=1
        return output
            
    
        
