class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(n)}
        for i,j in edges:
            preMap[i].append(j)
            preMap[j].append(i)
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for j in preMap[node]:
                if j == prev:
                    continue
                if not dfs(j,node):
                    return False
            return True
        return dfs(0,-1) and n == len(visited)
                
        