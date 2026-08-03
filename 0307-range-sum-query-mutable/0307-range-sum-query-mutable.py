class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums) + 1
        self.tree = [0] * self.n
        for i in range(1, self.n):
            self.tree[i] += nums[i - 1]
            j = i + self.lowbit(i)
            if j < self.n:
                self.tree[j] += self.tree[i]
        print(self.tree)
        self.nums = nums[:]
        # for i, num in enumerate(nums):
            # self.update(i, num)
    
    def lowbit(self, index: int) -> int:
        return index & (-index)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        index += 1
        while index < self.n:
            self.tree[index] += delta
            index += self.lowbit(index)
        
    def query(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= self.lowbit(index)
        return total

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right + 1) - self.query(left)        

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)