class Solution {
    public boolean isAnagram(String s, String t) {
        int[] count = new int[26];
        char[] sc = s.toCharArray();
        char[] tc = t.toCharArray();
        int s_n = sc.length;
        int t_n = tc.length;
        if (s_n != t_n) return false;
        for (int i =0; i < sc.length; i++) {
            count[sc[i] - 'a']++;
            count[tc[i] - 'a']--;
        }
        for (int j = 0; j < count.length; j++) {
            if (count[j] != 0) return false;
        }
        return true;
    }
}