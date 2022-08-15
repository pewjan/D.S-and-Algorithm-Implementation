class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        
        
        def dfs(sub, index, total):
            if total == target:
                output.append(sub[:])
                return
            if index >= len(candidates) or total > target:
                return 
            
            sub.append(candidates[index])
            dfs(sub, index, total + candidates[index])
            
            sub.pop()
            dfs(sub, index + 1, total)
            
        
        
        dfs([],0,0)
        return output
            
            
