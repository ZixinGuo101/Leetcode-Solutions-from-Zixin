class Fenwick_tree:
    def __init__(self, length):
        self.n = length
        self.tree = [0] * (self.n + 1)
    
    def lowbit(self, x):
        return x & -x
    
    def update(self, pos, val):
        while pos <= self.n:
            self.tree[pos] += 1
            pos += self.lowbit(pos)
    
    def query(self, pos):
        total = 0
        while pos > 0:
            total += self.tree[pos]
            pos -= self.lowbit(pos)
        return total

class Solution:
    def discrete(self, nums: List[int]) -> (List[int], List[int]):
        s = sorted(set(nums))
        m = {}
        for i, num in enumerate(s):
            m[num] = i + 1
        return [m[x] for x in nums], s
    
    def compare(self, c1, l1, c2, l2):
        if c1 > c2:
            return True
        elif c1 < c2:
            return False
        elif l1 > l2:
            return False
        else:
            return True
    
    def resultArray(self, nums: List[int]) -> List[int]:
        points, decoder = self.discrete(nums)
        n = len(decoder)
        arr1 = [nums[0]]
        tree1 = Fenwick_tree(n)
        tree1.update(points[0], 1)
        arr2 = [nums[1]]
        tree2 = Fenwick_tree(n)
        tree2.update(points[1], 1)
        for i in range(2, len(points)):
            # print(i, points[i])
            c1 = len(arr1) - tree1.query(points[i])
            c2 = len(arr2) - tree2.query(points[i])
            if self.compare(c1, len(arr1), c2, len(arr2)):
                arr1.append(nums[i])
                tree1.update(points[i], 1)
            else:
                arr2.append(nums[i])
                tree2.update(points[i], 1)
        arr1.extend(arr2)
        return arr1
