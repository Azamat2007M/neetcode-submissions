class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Sliding window method Time: O(n + m) Space: O(n + m)
        if not s or not t:
            return ""

        counterT = Counter(t)
        window = {}
        res, res_len = [-1, -1], float('inf')
        have, need = 0, len(counterT)
        l = 0

        for r, char in enumerate(s):
            window[char] = 1 + window.get(char, 0) 

            if char in counterT and window[char] == counterT[char]:
                have += 1
            
            while have == need:
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                window[s[l]] -= 1

                if s[l] in counterT and window[s[l]] < counterT[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l:r + 1] if res_len != float('inf') else ""