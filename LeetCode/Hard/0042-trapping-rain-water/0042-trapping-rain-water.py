class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2:
            return 0
        left = 1
        right = n - 2
        cnt = 0
        pre = height[0]
        suf = height[n-1]

        while left <= right:
            if pre > suf:
                if height[right] >= suf:
                    suf = height[right]
                else:
                    cnt += suf - height[right]
                right -= 1
            else:
                if height[left] >= pre:
                    pre = height[left]
                else:
                    cnt += pre - height[left]
                left += 1
            print(cnt)
        
        return cnt
        '''
                  -
        -         -
        -     -   -
        - -   - - -
        - -   - - -
        - - - - - -
        '''

        