class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    return False
                item = stack.pop()
                if i != hash_map[item]:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False



        