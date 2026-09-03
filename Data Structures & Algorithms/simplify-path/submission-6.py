class Solution:
    def simplifyPath(self, path: str) -> str:
        #Stack method with portions Time: O(n) Space: O(n)
        # stack = []
        # portions = path.split('/')

        # for p in portions:
        #     if '..' == p:
        #         if stack: stack.pop()
        #     elif '' == p or '.' == p:
        #         continue
        #     else:
        #         stack.append(p)
            
        # return '/' + '/'.join(stack)

        #Another method without portions
        stack = []
        n = len(path)
        i = 0

        while i < n:
            while i < n and path[i] == '/':
                i += 1
            
            start = i
            while i < n and path[i] != '/':
                i += 1
            
            portion = path[start:i]

            if portion == '..':
                if stack: stack.pop()
            elif portion != '' and portion != '.':
                stack.append(portion)

        return '/' + '/'.join(stack)