class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * n
        for b in bookings:
            ans[b[0] - 1] += b[2]
            if b[1] < n:
                ans[b[1]] -= b[2]
        
        for i in range(1, n):
            ans[i] = ans[i] + ans[i-1]
        
        return ans
        