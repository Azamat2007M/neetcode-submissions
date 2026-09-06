class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l, r = 0, length - 1

        while l < r:
            m = (l + r) // 2
            
            if mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1
            else:
                r = m

        peak = l
        l, r = 0, peak

        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m

        l, r = peak + 1, length - 1

        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m
        
        return -1