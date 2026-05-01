class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for c in s:
            if c in "([{":
                st.append(c)
            elif not st:
                return False
            elif c == ')':
                t = st.pop()
                if t != '(':
                    return False
            elif c == ']':
                t = st.pop()
                if t != '[':
                    return False
            else:
                t = st.pop()
                if t != '{':
                    return False
        if st:
            return False
        return True