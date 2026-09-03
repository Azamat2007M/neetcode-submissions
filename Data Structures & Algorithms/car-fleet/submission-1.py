class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        stack = []

        for pair in sorted(pairs)[::-1]:
            time = (target - pair[0]) / pair[1]
            stack.append(time)

            if len(stack) >= 2 and time <= stack[-2]:
                stack.pop()
            
        
        return len(stack)