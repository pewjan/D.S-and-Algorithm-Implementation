import collections
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        windowStart = 0
        largest = 0
        currentSum = 0
        for windowEnd in range(len(Arr)):
            currentSum+=Arr[windowEnd]
            if windowEnd >= K - 1:
                largest = max(currentSum, largest)
                currentSum -= Arr[windowStart]
                windowStart+=1
        return largest
                