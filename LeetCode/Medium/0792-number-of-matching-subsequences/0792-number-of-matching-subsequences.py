class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        # 对 s 进行预处理，记录 char -> 该 char 的索引列表
        charToIndexes = [[] for _ in range(26)]
        for i in range(len(s)):
            c = s[i]
            charToIndexes[ord(c) - ord('a')].append(i)

        res = 0
        for word in words:
            # 字符串 word 上的指针 i
            i = 0
            # 字符串 s 上的指针 j
            j = 0
            # 现在判断 word 是否是 s 的子序列
            # 借助 charToIndexes 查找 word 中每个字符在 s 中的索引
            while i < len(word):
                c = word[i]
                # 整个 s 压根儿没有字符 word[i]
                if not charToIndexes[ord(c) - ord('a')]:
                    break
                # 二分搜索大于等于 j 的最小索引
                # 即在 s[j..] 中搜索等于 word[i] 的最小索引
                pos = self.left_bound(charToIndexes[ord(c) - ord('a')], j)
                if pos == len(charToIndexes[ord(c) - ord('a')]):
                    break
                j = charToIndexes[ord(c) - ord('a')][pos]
                # 如果找到，即 word[i] == s[j]，继续往后匹配
                j += 1
                i += 1
            # 如果 word 完成匹配，则是 s 的子序列
            if i == len(word):
                res += 1

        return res

    # 查找左侧边界的二分查找
    def left_bound(self, arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if target > arr[mid]:
                left = mid + 1
            else:
                right = mid
        return left        