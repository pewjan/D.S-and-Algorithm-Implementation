class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited = set()
        cycle = set()
        output = []
        graph = self.buildGraph(prerequisites)
        
        
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True

            
            cycle.add(node)
            for nei in graph[node]:
                if dfs(nei) == False:
                    return False
            
            cycle.remove(node)
            visited.add(node)
            output.append(node)
            return True
            
            
            
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return output
        
        
    
    def buildGraph(self, prerequisites):
        graph = defaultdict(list)
        
        for p in prerequisites:
            a = p[0]
            b = p[1]
            graph[a].append(b)
        return graph
