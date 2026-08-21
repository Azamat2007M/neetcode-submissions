class Solution:
    def validPalindrome(self, s: str) -> bool:
        #Palindrom range method Time: O(n) Space: O(1)

        l, r = 0, len(s) - 1

        def is_palindrom_range(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
            
                l += 1
                r -= 1

            return True

        while l < r:
            if s[l] != s[r]:
                return is_palindrom_range(l + 1, r) or is_palindrom_range(l, r - 1)
            
            l += 1
            r -= 1
        
        return True

        #Another method with extra meomory Time: O(n) Space: O(n)
        # l, r = 0, len(s) - 1

        # while l < r:
        #     if s[l] != s[r]:
        #         skipL, skipR = s[l+1:r+1], s[l:r]
        #         return (skipL == skipL[::-1] or skipR == skipR[::-1])

        #     l += 1
        #     r -= 1
        
        # return True 