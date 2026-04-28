class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ans = []
        n = len(path)

        print(n)
        i = 1

        while i < n:
            if path[i] == '/':
                i += 1
                continue
            j = i
            print(i)
            while i < n and path[i] != '/':
                i += 1
            s = path[j:i]
            print(s)
            if s == '.' or s == '':
                i += 1
                continue
            elif s == "..":
                if len(ans) > 1:
                    ans.pop()
                    ans.pop()
                else:
                    i += 1
                    continue
            else:
                ans.append('/')
                ans.append(s)
            
            i += 1
        if not ans:
            ans.append('/')
        return ''.join(ans)


        