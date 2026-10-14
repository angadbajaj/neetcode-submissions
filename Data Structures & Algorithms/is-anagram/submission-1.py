class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map1 = {}
        hash_map2 = {}
        for i in s:
            hash_map1[i] = 1 + hash_map1.get(i, 0)
        for i in t:
            hash_map2[i] = 1 + hash_map2.get(i, 0)

        return hash_map1 == hash_map2  