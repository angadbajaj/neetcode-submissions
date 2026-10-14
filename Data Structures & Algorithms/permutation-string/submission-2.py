class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s1_length = len(s1)
        for i in range(0, len(s2)-len(s1)+1):
            sorted_sub = sorted(s2[i:i+s1_length])
            if sorted_sub == s1:
                return True
        return False