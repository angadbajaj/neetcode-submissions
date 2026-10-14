class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, n in enumerate(nums):
            seen = target - n
            if seen in res:
                return [res[seen], i]
            res[n] = i

        