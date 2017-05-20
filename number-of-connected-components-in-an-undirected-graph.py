class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = [0] * n
        g = {x: [] for x in range(n) } # create adjacency list
        # print(g)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        # print" Adjaceny list from given edges",(g)
        
        count = 0
        for node in range(n):
            if visited[node] == 0:
                self.dfs(node, g, visited)
                count += 1
                
        return count
        
        
    def dfs(self,node, g, visited):
        if visited[node]:
            return
        
        visited[node] = 1
        for nei in g[node]:
            self.dfs(nei, g, visited)
    