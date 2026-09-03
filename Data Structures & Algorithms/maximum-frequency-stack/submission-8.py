class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.maxctn = 0
        self.ctn = {}

    def push(self, val: int) -> None:
        valctn = 1 + self.ctn.get(val, 0)
        self.ctn[val] = valctn

        if self.maxctn < valctn:
            self.maxctn = valctn
            self.stacks[valctn] = []
        
        self.stacks[valctn].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxctn].pop()
        self.ctn[res] -= 1
        if not self.stacks[self.maxctn]:
            self.maxctn -= 1
        
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()