class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])

            i = end
        
        return res

        # Length-Prefix Time: O(n) Space: O(n)