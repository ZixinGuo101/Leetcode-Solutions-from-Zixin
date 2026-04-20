class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0
        r = n - 1
        v = 0
        max_l = 0
        max_r = 0

        while l < r:
            max_l = height[l] if height[l] > max_l else max_l
            max_r = height[r] if height[r] > max_r else max_r
            if max_l > max_r:
                v += max_r - height[r] if (max_r - height[r]) > 0 else 0
                r -= 1
            else:
                v += max_l - height[l] if (max_l - height[l] > 0) else 0
                l += 1
        
        return v

        