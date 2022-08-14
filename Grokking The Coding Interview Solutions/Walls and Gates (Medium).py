from collections import *
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        ROW = len(rooms)
        COL = len(rooms[0])
        queue = deque()
        visited = set()
        for r in range(ROW):
            for c in range(COL):
                if rooms[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r,c))
        
        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]
        distance = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                rooms[r][c] = distance
                for d in directions:
                    nr,nc = r+d[0], c+d[1]
                    if nr < 0 or nc < 0 or nr >= ROW or nc >= COL or (nr, nc) in visited or rooms[nr][nc] == -1:
                        continue
                    print([nr,nc])
                    visited.add((nr,nc))
                    queue.append([nr,nc])
            distance+=1
