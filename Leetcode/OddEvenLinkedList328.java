package Algorithms.Leetcode;

/**
 * Created by dianaluca on 11/11/16.
 */
public class OddEvenLinkedList328 {
  public static class ListNode implements java.io.Serializable {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
  }

  public static ListNode oddEvenList(ListNode head) {
    if (head == null || head.next == null || head.next.next == null) return head;
    ListNode node = head;
    ListNode even = new ListNode(head.next.val);
    ListNode evenTmp = even;

    node.next = node.next.next;
    while (node.next != null) {
      node = node.next;

      if (node.next == null) {
        node.next = even;
        return head;
      }
      else {
        evenTmp.next = node.next;
        evenTmp = evenTmp.next;
      }
    }
    return head;
  }

  /**
   * Test Client:
   * Your input: [1,2,3,4,5,6,7,8]
   * Expected answer: [1,3,5,7,2,4,6,8]
   */

  public static void main(String[] args) {
    ListNode linkedList = new ListNode(1);
    linkedList.next = new ListNode(2);
    linkedList.next.next = new ListNode(3);
    linkedList.next.next.next = new ListNode(4);
    linkedList.next.next.next.next = new ListNode(5);
    linkedList.next.next.next.next.next = new ListNode(6);
    linkedList.next.next.next.next.next.next = new ListNode(7);
    linkedList.next.next.next.next.next.next.next = new ListNode(8);
    linkedList = oddEvenList(linkedList);

    while (linkedList != null) {
      System.out.print(linkedList.val + ", ");
      linkedList = linkedList.next;
    }
  }
}
