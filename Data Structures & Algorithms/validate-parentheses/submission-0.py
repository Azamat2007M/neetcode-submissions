class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeB = {')': '(', ']': '[', '}': '{'}

        for b in s:
            if b in closeB:
                if stack and stack[-1] == closeB[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return not stack