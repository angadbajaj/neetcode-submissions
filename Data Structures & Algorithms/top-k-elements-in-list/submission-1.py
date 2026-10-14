class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        for i in nums:
            if i in freq_table:
                freq_table[i] += 1
            else:
                freq_table[i] = 1
        sorted_table = dict(sorted(freq_table.items(), key = lambda x:x[1], reverse = True))
        output_list = []
        for i in sorted_table:
            if k == 0:
                break
            output_list.append(i)
            k = k - 1
        return output_list


