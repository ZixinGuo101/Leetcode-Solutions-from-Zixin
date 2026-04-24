class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        ans = 0
        n = len(arr)

        for i in range(n-2):
            l = i + 1
            r = n - 1
            
            while l < r:
                # print(l, r)
                cnt = target - arr[i] - arr[l] - arr[r]
                if cnt > 0:
                    l += 1
                elif cnt < 0:
                    r -= 1
                else:
                    if arr[l] == arr[r]:
                        ans += (r-l+1)*(r-l)/2
                        l = r
                    else:
                        t = 1
                        ans += 1
                        while l < r and arr[l+1] == arr[l]:
                            l += 1
                            t += 1
                            ans += 1
                        while l < r and arr[r] == arr[r-1]:
                            r -= 1
                            ans += t
                        l += 1
                        r -= 1
                # print(ans)
        
        return (ans % (10**9+7))