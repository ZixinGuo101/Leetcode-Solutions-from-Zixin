class NumArray:

    def __init__(self, nums: List[int]):
        self._nums = nums
        self._tree = [ 0, *nums ]

        for index, number in enumerate(self._tree):
            index += index & -index
            if index < len(self._tree):
                self._tree[index] += number

    def update(self, index: int, val: int):
        previous = self._nums[index]
        self._nums[index] = val

        diff = val - previous
        index += 1
        while index < len(self._tree):
            self._tree[index] += diff
            index += index & -index


    def query(self, index: int) -> int:
        index += 1
        value = 0

        while index > 0:
            value += self._tree[index]
            index -= index & -index

        return value

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)