class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Stack method Time: O(nlogn) Space: O(n)
        pairs = [(p, s) for p, s in zip(position, speed)]
        stack = []

        for pair in sorted(pairs)[::-1]:
            time = (target - pair[0]) / pair[1]
            stack.append(time)

            if len(stack) >= 2 and time <= stack[-2]:
                stack.pop()
            
        
        return len(stack)

        #Another method without stack Time: O(nlogn) Space: O(1)
        # pairs = sorted(zip(position, speed), reverse=True)
        # fleets = 0
        # max_time = 0.0

        # for p, s in pairs:
        #     time = (target - p) / s

        #     if max_time < time:
        #         fleets += 1
        #         max_time = time
        
        # return fleets