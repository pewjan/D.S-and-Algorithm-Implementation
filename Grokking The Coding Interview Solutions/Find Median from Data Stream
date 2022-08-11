class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []
        heapq.heapify(self.smallHeap)
        heapq.heapify(self.largeHeap)
        

    def addNum(self, num: int) -> None:
        if not self.smallHeap or -self.smallHeap[0] >= num:
            heapq.heappush(self.smallHeap, (-1 * num))
        else:
            heapq.heappush(self.largeHeap, num)
            
            
            
            
        if len(self.smallHeap) > len(self.largeHeap)+ 1:
            value = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, value)
        elif len(self.largeHeap) > len(self.smallHeap) + 1:
            value = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -1 * value)           
        
            
        
        
        

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return (-1 * self.smallHeap[0])
        elif len(self.largeHeap) > len(self.smallHeap):
            return (self.largeHeap[0])
        else:
            return (((-1 * self.smallHeap[0]) + self.largeHeap[0])/2)
            
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
