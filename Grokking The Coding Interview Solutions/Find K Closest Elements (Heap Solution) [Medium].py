class Solution(object):
    def findClosestElements(self, arr, k, x):
        index = self.binarySearch(arr, x)
        left, right = index - k, index + k
        left = max(0, left)
        right = min(len(arr) - 1, right )
        

        minHeap = []
        
        for i in range(left, right+1):
            heapq.heappush(minHeap, [abs(arr[i] - x), arr[i]])
            
        
        output = []
        
        for i in range(k):
            output.append(heapq.heappop(minHeap)[1])
        
        output.sort()
        return output
        
        

    def binarySearch(self, arr, target):
        
        left = 0
        right = len(arr)-1
        
        while left <= right:
            mid = (left + right ) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
        if left > 0:
            left -= 1
        return left
        
        
