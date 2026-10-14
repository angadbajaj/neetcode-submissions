class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i,n in enumerate(nums):
            find = target - n
            if find in hash_map:
                return sorted([i, hash_map[find]])
            hash_map[n] = i
            
        