class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        hash_map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(len(s)):
            if i + 1 < len(s) and hash_map[s[i]] < hash_map[s[i+1]]:
                res -= hash_map[s[i]]
            else:
                res += hash_map[s[i]]
        return res