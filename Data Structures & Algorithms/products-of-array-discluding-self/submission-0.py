class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Prefix and Postfix method Time: O(2n) Space: O(n) Extra Space: O(1)
        n = len(nums)
        res = [1] * n
        prefix = 1

        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        #Another method Devision but we can't write Time: O(2n) Space: O(n) Extra Space: O(1)
        # m_num = 1
        # zero_count = 0
        # for num in nums:
        #     if num == 0:
        #         zero_count += 1
        #     else:
        #         m_num *= num
        
        # res = []

        # for num in nums:
        #     if zero_count > 1:
        #         res.append(0)
        #     elif zero_count == 1:
        #         res.append(m_num if num == 0 else 0)
        #     else:
        #         res.append(m_num // num)
            
        
        # return res