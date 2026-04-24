class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        car = [0] * 1001
        m = 0
        for t in trips:
            car[t[1]] += t[0]
            car[t[2]] -= t[0]
            m = t[2] if t[2] > m else m

        if car[0] > capacity:
            return False
        for i in range(1, m):
            car[i] += car[i-1]
            if car[i] > capacity:
                return False
        
        return True