class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #Another method with Stack Time: O(n) Space: O(n)
        stack = []

        for word in s:
            stack.append(word)

        for i in range(len(s)):
            s[i] = stack.pop()   
        
        return s