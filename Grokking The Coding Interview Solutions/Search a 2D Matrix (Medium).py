class Solution(object):
    def searchMatrix(self, matrix, target): 
        left = 0
        right = len(matrix) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][-1] < target:
                left = mid + 1
                
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                break
        if not (left <= right):
            return False
        row = (left + right) // 2
        
        left, right = 0, len(matrix[0])
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
            
        
