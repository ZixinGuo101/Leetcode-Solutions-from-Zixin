class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position, speed), key = lambda x : x[0])
        n = len(position)
        stk = []
        res = 0
        for i in range(n-1, -1, -1):
            t = float(target - cars[i][0]) / cars[i][1]
            if stk and t <= stk[-1]:
                continue
            stk.append(t)
        return len(stk)
