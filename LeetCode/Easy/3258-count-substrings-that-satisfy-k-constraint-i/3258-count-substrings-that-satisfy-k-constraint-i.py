class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt0 = 0
        cnt1 = 0
        left = 0
        ans  = 0

        for right, c in enumerate(s):
            cnt0 += 1 - int(c)
            cnt1 += int(c)

            while cnt0 > k and cnt1 > k:
                cnt0 -= 1 - int(s[left])
                cnt1 -= int(s[left])
                left += 1
            
            ans += right - left + 1
        
        return ans