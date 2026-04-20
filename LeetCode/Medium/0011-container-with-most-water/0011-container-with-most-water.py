class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n-1
        area = 0

        while left < right:
            l = right - left
            if height[left] > height[right]:
                h = height[right]
                right -= 1
            else:
                h = height[left]
                left += 1
            area = l * h if l * h > area else area
        
        return area
        