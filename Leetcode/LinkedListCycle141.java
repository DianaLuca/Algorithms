package Algorithms.Leetcode;

/**
 * Given a linked list, determine if it has a cycle in it.
 * Follow up:
 * Can you solve it without using extra space?
 *
 * Floyd's tortoise and the hare algorithm moves two pointers at different speeds
 * through the sequence of values until they both point to equal values.
 *
 * Created by dianaluca on 10/1/16.
 */

public class LinkedListCycle141 {
  public class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
      val = x;
      next = null;
    }
  }

  public boolean hasCycle(ListNode head) {
    if (head == null) return false;
    ListNode slow, fast;
    slow = fast = head;

    while (true) {
      slow = slow.next;

      if (fast.next == null) return false;
      else fast = fast.next.next;

      if (slow == null || fast == null) return false;

      if (slow == fast) return true;  //if the 2 nodes ever meet, means we have a loop
    }
  }
}
