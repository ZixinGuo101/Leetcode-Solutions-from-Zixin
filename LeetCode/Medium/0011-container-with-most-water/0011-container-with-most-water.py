class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n - 1
        res = 0

        while left < right:
            l = right - left
            if height[right] < height[left]:
                h = height[right]
                right -= 1
            else:
                h = height[left]
                left += 1
            res = l*h if l*h > res else res
        
        return res
        