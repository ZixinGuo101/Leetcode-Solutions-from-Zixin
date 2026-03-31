/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode dummySmall = new ListNode(-1), tailSmall = dummySmall;
        ListNode dummyLarge = new ListNode(-1), tailLarge = dummyLarge;
        ListNode p = head;

        while (p != null) {
            if (p.val < x) {
                tailSmall.next = p;
                tailSmall = tailSmall.next;
            } else {
                tailLarge.next = p;
                tailLarge = tailLarge.next;
            }

            ListNode temp = p;
            p = p.next;
            temp.next = null;
        }

        tailSmall.next = dummyLarge.next;
        return dummySmall.next;
    }
}