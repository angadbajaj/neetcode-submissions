class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum())
        s = s.lower()
        i,j = 0, len(s) - 1
        while j >= i:
            if s[i] == s[j]:
                i +=1
                j -=1
            else:
                return False
        return True
