class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        skip = False
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue
                
                if stack[-1] == abs(a):
                    stack.pop()

                skip = True
                break

            if skip:
                skip = False
                continue
            
            stack.append(a)
        
        return stack
                
