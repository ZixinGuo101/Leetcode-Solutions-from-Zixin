class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if s.count('1') < k:
            return ''
        
        left = 0
        cnt1 = 0
        min_len = float('inf')
        left_sub = []
        len_sub = []
        ans = ''


        for right, c in enumerate(s):
            cnt1 += int(c)

            while s[left] == '0' or cnt1 > k:
                cnt1 -= int(s[left])
                left += 1
            
            l = right - left + 1
            if l <= min_len and cnt1 == k:
                len_sub.append(l)
                left_sub.append(left)
                min_len = l
        # print(len_sub)
        # print(left_sub)
        # print(min_len)
        for i in range(len(len_sub)):
            if len_sub[i] == min_len and (ans == '' or s[left_sub[i] : left_sub[i] + min_len] < ans):
                ans = s[left_sub[i] : left_sub[i] + min_len]
                # print(ans)
        
        return ans
