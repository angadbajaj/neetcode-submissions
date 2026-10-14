class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0
        output_list = []
        for i in nums:
            if i == 0:
                zero_count += 1
        if zero_count == 0:
            for i in nums:
                total = total * i
            for i in nums:
                output_list.append(total // i)
        elif zero_count == 1:
            output_list = [0] * len(nums)
            index = 0
            for i,v in enumerate(nums):
                if v == 0:
                    index = i
                else:
                    total = total * v
            output_list[index] = total
        else:
            output_list = [0] * len(nums)

        return output_list

        