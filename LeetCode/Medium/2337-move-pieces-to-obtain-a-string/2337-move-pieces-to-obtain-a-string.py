class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        if start.replace('_', '') != target.replace('_', ''):
            return False
        j = 0
        for i, c in enumerate(start):
            if c == '_':
                continue
            while target[j] == '_':
                j += 1
            if c == 'L':
                if i < j:
                    return False
            else:
                if i > j:
                    return False
            j += 1
        
        return True
        