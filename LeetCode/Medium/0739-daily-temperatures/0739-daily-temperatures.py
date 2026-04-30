class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        res = [0] * n
        st = []
        for i in range(n):
            while st and temperatures[i] > temperatures[st[-1]]:
                prev = st.pop()
                res[prev] = i - prev
            st.append(i)
        
        return res