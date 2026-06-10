class Solution(object):
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        """
        :type chargeTimes: List[int]
        :type runningCosts: List[int]
        :type budget: int
        :rtype: int
        """
        n = len(chargeTimes)
        maxq = deque()
        res = 0
        first = 0
        costs = 0
        for last in range(n):
            while maxq and chargeTimes[maxq[-1]] <= chargeTimes[last]:
                maxq.pop()
            maxq.append(last)
            costs += runningCosts[last]
            while first <= last and (chargeTimes[maxq[0]] + (last - first + 1) * costs) > budget:
                if first == maxq[0]:
                    maxq.popleft()
                costs -= runningCosts[first]
                first += 1
            res = max(res, last - first + 1)
        return res