class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j, i = 0, 1
        res = []
        
        while len(numbers) > i and len(numbers) > j:
            if (numbers[i] + numbers[j]) == target:
                res.append(j + 1)
                res.append(i + 1)

                break
            elif numbers[i] + numbers[j] < target:
                i += 1
                j += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
        
        return res