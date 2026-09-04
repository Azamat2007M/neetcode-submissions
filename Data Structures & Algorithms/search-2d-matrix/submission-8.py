class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary search method Time: O(log(n*m)) Space: 1
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n * m - 1

        while left <= right:
            mid = (left + right) // 2
            r, c = mid // n, mid % n

            if target > matrix[r][c]:
                left = mid + 1
            elif target < matrix[r][c]:
                right = mid - 1
            else:
                return True
            
        return False

        #Another Binary search method Time: O(log(n*m)) Space: 1
        # top, bot = 0, len(matrix) - 1

        # while top <= bot:
        #     row = (top + bot) // 2

        #     if target > matrix[row][-1]:
        #         top = row + 1
        #     elif target < matrix[row][0]:
        #         bot = row - 1
        #     else:
        #         break
        
        # if not (top <= bot):
        #     return False
        
        # l, r = 0, len(matrix[0]) - 1

        # while l <= r:
        #     mid = (r + l) // 2

        #     if target > matrix[row][mid]:
        #         l = mid + 1
        #     elif target < matrix[row][mid]:
        #         r = mid - 1
        #     else:
        #         return True
        
        # return False