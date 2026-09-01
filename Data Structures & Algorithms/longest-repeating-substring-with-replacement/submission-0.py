class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Sliding window + Hash Map method Time: O(n) Space: O(m) (m == 26)
        window = defaultdict(int)
        maxf, l, res = 0, 0, 0

        for r, char in enumerate(s):
            window[char] += 1
            maxf = max(maxf, window[char])

            while (r - l + 1) - maxf > k:
                window[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res