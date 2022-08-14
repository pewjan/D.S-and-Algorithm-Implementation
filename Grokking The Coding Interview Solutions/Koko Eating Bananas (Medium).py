class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1 
        right = max(piles)
        time = float("infinity")
        
        while left <= right:
            mid = (left + right) // 2
            hour = 0
            for pile in piles:
                hour += (((pile - 1)//mid)+1)
            
            if hour <= h:
                time = min(mid, time)
                right = mid - 1
            else:
                left = mid + 1
        return time
                
                
