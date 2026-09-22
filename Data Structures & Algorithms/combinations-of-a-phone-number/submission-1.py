class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Iterative method Time: O(n*4^n) Space: O(n)
        if not digits:
            return []

        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = [""]

        for digit in digits:
            tmp = []
            for current_s in res:
                for c in digit_to_char[digit]:
                    tmp.append(current_s + c)

            res = tmp
        return res

        #Backtracking method Time: O(n*4^n) Space: O(n)
        # if not digits:
        #     return []

        # digit_to_char = {
        #     "2": "abc",
        #     "3": "def",
        #     "4": "ghi",
        #     "5": "jkl",
        #     "6": "mno",
        #     "7": "pqrs",
        #     "8": "tuv",
        #     "9": "wxyz"
        # }
        
        # res = []

        # def backtracking(current_str: str, i: int) -> None:
        #     if len(current_str) == len(digits):
        #         res.append(current_str)
        #         return
            
        #     for char in digit_to_char[digits[i]]:
        #         backtracking(current_str + char, i + 1)
        
        # backtracking("", 0)
        # return res