class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # 2 5 8 9
        # 4 7


        def find(ns1, ns2):
            m = len(ns1)
            n = len(ns2)
            ans = 0
            i = 0

            while i < m:
                j = 0
                k = n-1
                t = ns1[i] * ns1[i]
                r = 0
                while j < k:
                    if ns2[j] * ns2[k] > t:
                        k -= 1
                    elif ns2[j] * ns2[k] < t:
                        j += 1
                    else:
                        if ns2[j] == ns2[k]:
                            r += (k-j)*(k-j+1)/2
                            j = k
                        else:
                            r += 1
                            cnt = 1
                            while j < k and ns2[j] == ns2[j+1]:
                                j += 1
                                r += 1
                                cnt += 1
                            while j < k and ns2[k] == ns2[k-1]:
                                k -= 1
                                r += cnt
                            j += 1
                            k -= 1
                ans += r
                i += 1
                if i < m and ns1[i] == ns1[i-1]:
                    ans += r
                    i += 1
            
            return ans

        nums1.sort()
        nums2.sort()
        return find(nums1, nums2) + find(nums2, nums1)
        # 1 1 4 4 12
        # 2 3 4 5
