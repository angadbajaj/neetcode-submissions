class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dict = defaultdict(list)
        for i in strs:
            sorted_s = ''.join(sorted(i))
            final_dict[sorted_s].append(i)
        return list(final_dict.values())
        