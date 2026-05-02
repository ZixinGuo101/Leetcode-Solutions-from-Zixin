class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0 # 一共需要的左右括号
        right = 0 # 匹配前面左括号需要的右括号

        for c in s:
            if c == '(':
                right += 2
                if right % 2 == 1:
                    right -= 1
                    ans += 1
            elif c == ')':
                if right == 0:
                    right += 1
                    ans += 1
                elif right != 0:
                    right -= 1
        
        return ans + right
