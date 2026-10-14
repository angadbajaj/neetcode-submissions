class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = {i:[]for i in range(n)}
        visit = [False]*n
        for u,v in edges:
            preMap[u].append(v)
            preMap[v].append(u)
        def dfs(node):
            for i in preMap[node]:
                if not visit[i]:
                    visit[i] = True
                    dfs(i)
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res+=1
        return res
        