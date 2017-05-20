class Solution(object):
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        
        g = {i: [] for i in range(n)}
        
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
            
        print(g)
        stack = [0]
        while stack:
            print(stack)
            stack += g.pop(stack.pop(), [])
            print(g)
            print()
            

        return not g