// Two pass

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // create a dummy
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        int length = 0;
        ListNode first = head;
        while(first !== null){
            length ++;
            first = first.next;
        }
        
        length -= n;
        first = dummy;
        while (length > 0){
            length --;
            first = first.next;
        }
        first.next = first.next.next;
        return dummy.next;
    }
}

// TC: O(L), SC:O(1)

// Explanation from solution:
// Complexity Analysis
//Time complexity : O(L).
// The algorithm makes two traversal of the list, first to calculate list length LL and second to find the (L - n)(L−n) th node. There are 2L-n2L−n operations and time complexity is O(L)O(L).
