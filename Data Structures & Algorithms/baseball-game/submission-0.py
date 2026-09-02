class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #Stack method Time: O(n) Space: O(n)
        stack = []

        for op in operations:
            if "+" == op:
                stack.append(stack[-1] + stack[-2])
            elif "D" == op:
                stack.append(stack[-1] * 2)
            elif "C" == op:
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)