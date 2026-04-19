class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        len_sub = []
        min_len = float('inf')
        cnt_k = 0
        left_sub = []
        left = 0

        for right, c in enumerate(s):
            if c == '1':
                cnt_k += 1
            
            while left <= right and cnt_k == k:
                l = right - left + 1
                if l <= min_len:
                    left_sub.append(left)
                    len_sub.append(l)
                    min_len = l
                if s[left] == '1':
                    cnt_k -= 1
                left += 1

        if min_len == float('inf'):
            return ""
        
        res_left = []
        for i in range(len(len_sub)):
            if len_sub[i] == min_len:
                res_left.append(left_sub[i])
        
        res = '1'*min_len
        for i in range(len(res_left)):
            if s[res_left[i]:(res_left[i]+min_len)] < res:
                res = s[res_left[i]:(res_left[i]+min_len)]
        
        return res
            