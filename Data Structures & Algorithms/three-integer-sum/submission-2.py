class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output_list = []
        nums = sorted(nums)
        seen = set()
        for index, target in enumerate(nums):
            i, j = index + 1, len(nums) - 1
            if target in seen:
                continue
            else:
                seen.add(target)
            while i < j:
                if nums[i] + nums[j] == -target:
                    output_list.append([nums[i], nums[j], target])
                    i +=1
                    j -=1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    if nums[i] + nums[j] < -target:
                        i += 1
                    else:
                        j -= 1
        return output_list

            



        