package Algorithms.Leetcode;

/**
 * Created by dianaluca on 9/16/16.
 */

public class ReverseLinkedList206 {
  public ListNode reverseListIterative(ListNode head) {
    if (head == null) return null;
    ListNode before = null;
    ListNode tmp = head;
    while (tmp != null) {
      ListNode next = tmp.next;
      tmp.next = before;
      before = tmp;
      tmp = next;
    }
    head = before;

    return head;
  }

  public ListNode reverseListRecursive(ListNode head) {
    if (head == null) return null;
    if (head.next == null) return head;

    ListNode nod = reverseListRecursive(head.next);
    head.next.next = head;
    head.next = null;
    return nod;
  }

  public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
  }


}
