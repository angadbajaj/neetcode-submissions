class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')':'(',']':'[','}':'{'}
        stack = []
        for bracket in s:
            if bracket in close_to_open:
                if stack:
                    item = stack.pop()
                    if item == close_to_open[bracket]:
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(bracket)
        if stack:
            return False
        else:
            return True
                    
        