class Solution(object):
    def findCircleNum(self, M):
        """
        Time - O(n2)[complete matrix is traversed] Space = O(n)[visited array]
        Consider the matrix as an adjacency matrix.
        Problem reduces to - finding the number of connected components in an undirected graph.
        Use dfs to visit each node. 
        Thus, to find the number of connected components, we start from every node which isn't visited right now and apply DFS starting with it. We increment the countcount of connected components for every new starting node.
        """
        visited = [0 for i in range(len(M))]
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                self.dfs(M, visited, i)
                count += 1
        return count
        
        
        
    def dfs(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M, visited, j)