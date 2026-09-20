class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Backtracking method Time: O(4^n/sqrt(n)) Space: O(n)
        res = []
        stack = []

        def backtracking(open: int, close: int) -> None:
            if open == close == n:
                res.append("".join(stack))
                return

            if open < n:
                stack.append('(')
                backtracking(open + 1, close)
                stack.pop()

            if close < open:
                stack.append(')')
                backtracking(open, close + 1)
                stack.pop()

        backtracking(0, 0)
        return res