class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        m = n - k
        win_c = 0


        for i in range(m):
            win_c += cardPoints[i]
        
        min_win = sum_c = win_c
        for i in range(m, n):
            sum_c += cardPoints[i]
            win_c += cardPoints[i] - cardPoints[i-m]
            min_win = min_win if min_win < win_c else win_c
        
        return sum_c - min_win