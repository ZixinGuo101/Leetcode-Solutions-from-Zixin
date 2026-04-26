class Solution(object):
    def canTransform(self, start, result):
        """
        :type start: str
        :type result: str
        :rtype: bool
        """
        sl = 0
        rl = 0
        n = len(start)

        while sl < n and rl < n:
            while sl < n and start[sl] == 'X':
                sl += 1
            
            while rl < n and result[rl] == 'X':
                rl += 1

            if sl < n and rl < n:
                if start[sl] != result[rl]:
                    return False
                elif start[sl] == 'L' and sl < rl:
                    return False
                elif start[sl] == 'R' and sl > rl:
                    return False
                else:
                    sl += 1
                    rl += 1

        while sl < n and start[sl] == 'X':
            sl += 1
        while rl < n and result[rl] == 'X':
            rl += 1

        return rl == sl