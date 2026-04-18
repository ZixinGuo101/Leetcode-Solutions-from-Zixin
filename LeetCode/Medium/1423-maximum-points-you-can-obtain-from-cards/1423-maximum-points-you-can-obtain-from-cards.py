class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        min_sum = 0
        n = len(cardPoints)
        m = n - k
        sub_sum = 0
        

        for i in range(m):
            sub_sum += cardPoints[i]
        min_sum = sub_sum
        card_sum = sub_sum
        for i in range(m,n):
            card_sum += cardPoints[i]
            sub_sum += cardPoints[i] - cardPoints[i-m]
            min_sum = min(min_sum, sub_sum)
        
        return card_sum - min_sum
        