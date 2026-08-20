class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #Two Pointers method Time: O(n+m) Space: O(n+m)
        res = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            res.append(word1[i]) 
            res.append(word2[j])
            i += 1
            j += 1
        
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)

        #Another method with zip_longest Time: O(n+m) Space: O(n+m)
        # res = []

        # for char1, char2 in zip_longest(word1, word2, fillvalue=''):
        #     res.append(char1)
        #     res.append(char2)
        
        # return ''.join(res)