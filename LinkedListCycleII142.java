package LeetCodeAlgorithms;

import java.util.HashSet;

/**
 * Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
 * Note: Do not modify the linked list.
 *
 * Follow up:
 * Can you solve it without using extra space?
 *
 * Created by dianaluca on 10/2/16.
 */

public class LinkedListCycleII142 {

  class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
      val = x;
      next = null;
    }
  }

  public class Solution {

    // Solution 1: O(N)
    public ListNode detectCycle(ListNode head) {
      if (head == null) return null;

      HashSet<ListNode> hm = new HashSet<>();

      while (hm.contains(head) != true) {
        hm.add(head);
        head = head.next;

        if (head == null)
          return null;
      }

      return head;
    }
  }

  // Solution 2: without using extra space
  public ListNode detectCycleMem1(ListNode head) {
    if (head == null) return null;

    ListNode slow, fast;
    slow = fast = head;
    boolean start = true;

    while (start || slow != fast) {
      if (fast == null  || fast.next == null) //don't need to check for slow since is slower
        return null;
      slow = slow.next;
      fast = fast.next.next;
      start = false;
    }

    while (head != slow) { //The math from behind: a = k(b+c) + c
      head = head.next;
      slow = slow.next;
    }

    return head;
  }
}
