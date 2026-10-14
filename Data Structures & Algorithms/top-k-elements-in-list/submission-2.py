class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        freq_bucket = [[] for i in range(len(nums)+1)]
        for i in nums:
            if i in freq_table:
                freq_table[i] += 1
            else:
                freq_table[i] = 1
        for n, c in freq_table.items():
            freq_bucket[c].append(n)
        output_list = []
        i = len(freq_bucket) - 1
        while i > 0:
            for n in freq_bucket[i]:
                if k == 0:
                    break
                output_list.append(n)
                k = k - 1
            i = i-1
        return output_list


