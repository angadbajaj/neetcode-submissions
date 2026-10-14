class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i,n in enumerate(nums):
            find = target - n
            if find in hash_map:
                if i < hash_map[find]:
                    return [i, hash_map[find]]
                else:
                    return [hash_map[find], i]
            hash_map[n] = i
            
        