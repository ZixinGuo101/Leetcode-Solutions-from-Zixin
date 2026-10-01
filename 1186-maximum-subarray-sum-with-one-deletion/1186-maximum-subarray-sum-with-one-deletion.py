class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        ans = arr[0]
        n = len(arr)
        dp_no_delete = arr[0]
        dp_delete = 0
        for i in range(1, n):
            temp = dp_delete
            dp_delete = max(dp_no_delete, arr[i] + dp_delete)
            dp_no_delete = arr[i] + max(dp_no_delete, 0)
            ans = max(ans, dp_delete, dp_no_delete)
        return ans