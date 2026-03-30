class Solution {
    public int subarraySum(int[] nums, int k) {
        int n = nums.length;
        HashMap<Integer, Integer> preSum = new HashMap<>();
        preSum.put(0, 1);
        int res = 0;
        int sum_i = 0;
        for (int i = 1; i <= n; i++) {
            sum_i += nums[i - 1];
            int sum_j = sum_i - k;
            if (preSum.containsKey(sum_j)) res += preSum.get(sum_j);
            preSum.put(sum_i, preSum.getOrDefault(sum_i, 0) + 1);
        }

        return res;
    }
}