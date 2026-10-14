class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix) - 1
        for i in matrix:
            for j in i:
                if j == target:
                    return True
        return False
            
        