class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        res = k
        count = 0

        for right, c in enumerate(blocks):
            if c =='W':
                count += 1
            
            left = right - k + 1
            if left < 0:
                continue
            
            res = min(res, count)

            if blocks[left] == 'W':
                count -= 1
            left += 1
        
        return res
        