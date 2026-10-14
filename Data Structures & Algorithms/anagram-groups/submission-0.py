class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dict = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            final_dict[sortedS].append(s)
        return list(final_dict.values())
        return [[""]]

        