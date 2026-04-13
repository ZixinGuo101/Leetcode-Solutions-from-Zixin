class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        finish = len(numbers) - 1
        start = 0
        res = [0] * 2
        while finish > start:
            if numbers[finish] + numbers[start] == target:
                res[0] = start + 1
                res[1] = finish + 1
                return res
            elif numbers[finish] + numbers[start] > target:
                finish -= 1
            else:
                start += 1
        
        