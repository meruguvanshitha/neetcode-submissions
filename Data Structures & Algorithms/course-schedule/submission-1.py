class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        vis = [0] * numCourses  # 0: unvisited, 1: visiting, 2: visited

        def dfs(i):
            if vis[i] == 1: return False  # Cycle found!
            if vis[i] == 2: return True   # Already verified safe
            
            vis[i] = 1
            for pre in adj[i]:
                if not dfs(pre): return False
            vis[i] = 2
            
            return True

        return all(dfs(i) for i in list(range(numCourses)))