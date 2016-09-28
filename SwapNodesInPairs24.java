package LeetCodeAlgorithms;

/**
 * Given a linked list, swap every two adjacent nodes and return its head.
 * For example,
 * Given 1->2->3->4, you should return the list as 2->1->4->3.
 * Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
 *
 * Created by dianaluca on 9/25/16.
 */

public class SwapNodesInPairs24 {
  public class ListNode {
    int val;
    ListNode next;
    ListNode (int x) {
      val = x;
    }
  }

  public ListNode swapPairs(ListNode head) {
    if (head == null || head.next == null) return head;

    //reverse first 2 nodes
    ListNode current = head.next;
    head.next = current.next;
    current.next = head;
    head = current;

    current = head.next;
    while (current.next != null && current.next.next != null) {
      ListNode temp = current.next.next;
      temp.next = current.next;
      current = temp.next;

    }
    return head;
  }
}
