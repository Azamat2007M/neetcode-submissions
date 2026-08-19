class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #Two-pointers method Time: O(n) Space: O(1)
        
        left, right = 0, len(s) - 1

        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s

        #Another method with Stack Time: O(n) Space: O(n)
        # stack = []

        # for word in s:
        #     stack.append(word)

        # for i in range(len(s)):
        #     s[i] = stack.pop()   
        
        # return s