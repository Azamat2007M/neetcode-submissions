class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #Backtracking method Time: O(n*2^n) Space: O(n)
        res = []
        part = []

        def isPalindrome(subset: str) -> bool:
            return subset == subset[::-1]

        def backtracking(start: int) -> None:
            if start == len(s):
                res.append(part.copy())
                return
            
            for end in range(start, len(s)):
                subset = s[start:end + 1]

                if isPalindrome(subset):
                    part.append(subset)
                    backtracking(end + 1)
                    part.pop()

        backtracking(0)
        return res