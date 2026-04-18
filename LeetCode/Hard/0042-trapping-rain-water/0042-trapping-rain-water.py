class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n - 1
        pre_max = 0
        suf_max = 0
        area = 0

        while left < right:
            pre_max = pre_max if pre_max > height[left] else height[left]
            suf_max = suf_max if suf_max > height[right] else height[right]
            if pre_max < suf_max:
                area += pre_max - height[left]
                left += 1
            else:
                area += suf_max - height[right]
                right -= 1
        
        return area
        
        