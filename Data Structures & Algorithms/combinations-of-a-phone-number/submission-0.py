class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        
        res = []

        def backtracking(current_str: str, i: int) -> None:
            if len(current_str) == len(digits):
                res.append(current_str)
                return
            
            for char in digit_to_char[digits[i]]:
                backtracking(current_str + char, i + 1)
        
        backtracking("", 0)
        return res