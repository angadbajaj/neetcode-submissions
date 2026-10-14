class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        output = []
        visitSet, CycleSet = set(), set()

        def dfs(crs):
            if crs in CycleSet:
                return False
            if crs in visitSet:
                return True
            CycleSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.add(crs)
            CycleSet.remove(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return []
        return output