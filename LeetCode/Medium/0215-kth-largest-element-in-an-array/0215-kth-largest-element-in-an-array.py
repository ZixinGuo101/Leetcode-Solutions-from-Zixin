class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums, l, r):
            i = randint(left, right)
            pivot = nums[i]
            # print(pivot, i)
            nums[i], nums[left] = nums[left], nums[i]
            i, j = left + 1, right
            while True:
                while i <= j and nums[i] < pivot:
                    i += 1
                # 此时 nums[i] >= pivot

                while i <= j and nums[j] > pivot:
                    j -= 1
                # 此时 nums[j] <= pivot

                if i >= j:
                    break

                # 维持循环不变量
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            nums[left], nums[j] = nums[j], nums[left]
            return j
        
        n = len(nums)
        target_index = n - k  # 第 k 大元素在升序数组中的下标是 n - k
        left, right = 0, n - 1  # 闭区间
        while True:
            i = partition(nums, left, right)
            # print(i, nums[i], left, right)
            if i == target_index:
                # 找到第 k 大元素
                return nums[i]
            if i > target_index:
                # 第 k 大元素在 [left, i - 1] 中
                right = i - 1
            else:
                # 第 k 大元素在 [i + 1, right] 中
                left = i + 1