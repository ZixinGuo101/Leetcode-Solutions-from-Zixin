class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n= len(height)
        area = 0
        pre = [0] * n
        suf = [0] * n
        pre[0] = height[0]
        suf[n-1] = height[n-1]

        for i in range(1, n):
            pre[i] = pre[i-1] if pre[i-1] > height[i] else height[i]
            suf[n-i-1] = suf[n-i] if suf[n-i] > height[n-i-1] else height[n-i-1]
        
        for i in range(n):
            cnt = min(pre[i], suf[i]) - height[i]
            area += cnt
        
        return area
        