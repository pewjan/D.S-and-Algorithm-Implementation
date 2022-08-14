from typing import (
    List,
)
from collections import *

class Solution:
    """
    @param target_map: 
    @return: 
    """
    def shortest_path(self, target_map: List[List[int]]) -> int:
        ROW = len(target_map)
        COL = len(target_map[0])        
        visited = set()
        queue = deque()
        queue.append([0,0])
        steps = 0
        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]
        while queue:
            for i in range(len(queue)):
                
                r, c = queue.popleft()
                visited.add((r,c))
                if target_map[r][c] == 2:
                    return steps
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if nr < 0 or nc < 0 or nr >= ROW or nc >= COL or target_map[nr][nc] == 1 or (nr,nc) in visited:
                        continue
                    queue.append([nr,nc])
                    
            steps +=1
        return -1
       

