class Solution(object):
    def kClosest(self, points, k):
        minHeap = []
        heapq.heapify(minHeap)
        output = []
        
        for point in points:
            distance = sqrt((point[0] * point[0]) + (point[1] * point[1]))
            heapq.heappush(minHeap, [distance, point[0], point[1]])
        
        while k > 0:
            output.append(heapq.heappop(minHeap)[1:])
            k-=1
        return output
        
        
