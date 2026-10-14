class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack:
                    item = stack.pop()
                    if item == closeToOpen[c]:
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False



        