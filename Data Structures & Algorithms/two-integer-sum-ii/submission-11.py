class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j, i = 0, 1
        res = []
        
        while len(numbers) > i and len(numbers) > j:
            if (numbers[i] + numbers[j]) == target:
                return [j + 1, i + 1]
            elif numbers[i] + numbers[j] < target:
                i += 1
                j += 1
            else:
                j -= 1