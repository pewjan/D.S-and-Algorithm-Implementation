from collections import deque


def bfs(graph, startingPos):
  Q = deque(startingPos)
  while Q:
    val = Q.popleft()
    print(val)
    for i in range(len(graph[val])):
      Q.append(graph[val][i])
    
  
    
  



graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

bfs(graph, "a")
