class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        windowDict = defaultdict(int)
        windowStart = 0 
        maxFruit = 0
        
        for windowEnd in range(len(fruits)):
            windowDict[fruits[windowEnd]]+=1
            
            
            while len(windowDict.keys()) > 2:
                if windowDict[fruits[windowStart]] == 1:
                    del windowDict[fruits[windowStart]]
                else:
                    windowDict[fruits[windowStart]] -=1
                windowStart+=1

            maxFruit = max(maxFruit, windowEnd - windowStart + 1)
        
        return maxFruit
            
                
