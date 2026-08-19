class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for word in s:
            if word.isalnum():
                new_str += word.lower()
        
        return new_str == new_str[::-1]

        #Two Pointers Time: O(n) Space: O(1)
    #     l, r = 0, len(s) - 1

    #     while l < r:
    #         while l < r and not self.isAlphaNum(s[l]):
    #             l += 1

    #         while l < r and not self.isAlphaNum(s[r]):
    #             r -= 1
            
    #         if s[l].lower() != s[r].lower():
    #             return False

    #         l += 1
    #         r -= 1
        
    #     return True

    # def isAlphaNum(self, char):
    #     return (
    #         ord('A') <= ord(char) <= ord('Z') or
    #         ord('a') <= ord(char) <= ord('z') or
    #         ord('0') <= ord(char) <= ord('9'))

    