class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        res = [0] * n
        st = []

        for i in range(n-1, -1, -1):
            while st and temperatures[i] >= temperatures[st[-1]]:
                st.pop()
            if st:
                res[i] = st[-1] - i
            else:
                res[i] = 0
            st.append(i)
        
        return res
            