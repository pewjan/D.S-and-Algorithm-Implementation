def dfs(graph, startingPos):
  stack = [startingPos]
  output = []
  while stack:
    currentVal = stack.pop()
    print(currentVal)
    for i in range(len(graph[currentVal])):
      stack.append(graph[currentVal][i])
  print(output)
    
  



graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

dfs(graph, "a")
