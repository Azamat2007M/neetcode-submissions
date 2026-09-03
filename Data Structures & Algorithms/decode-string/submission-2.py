class Solution:
    def decodeString(self, s: str) -> str:
        #Stack with backtracking Time: O(m) Space: O(m)
        # stack = []

        # for c in s:
        #     if c != ']':
        #         stack.append(c)
        #     else:
        #         substr = ''

        #         while stack and stack[-1] != '[':
        #             substr = stack.pop() + substr
        #         stack.pop()

        #         k = ''

        #         while stack and stack[-1].isdigit():
        #             k = stack.pop() + k
                
        #         stack.append(int(k) * substr)

        # return ''.join(stack)

        #Another method Time: O(m) Space: O(m)
        stack = []
        substr = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                stack.append((substr, k))
                substr = ''
                k = 0
            elif c == ']':
                prev_s, prev_k = stack.pop()
                substr = prev_s + prev_k * substr
            else:
                substr += c

        return substr