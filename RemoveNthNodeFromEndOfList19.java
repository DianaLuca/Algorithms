package LeetCodeAlgorithms;

/**
 * Given a linked list, remove the nth node from the end of list and return its head.
 *
 * For example,
 * Given linked list: 1->2->3->4->5, and n = 2.
 * After removing the second node from the end, the linked list becomes 1->2->3->5.
 *
 * Created by dianaluca on 11/9/16.
 */


public class RemoveNthNodeFromEndOfList19 {

  public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
  }

  public ListNode removeNthFromEnd(ListNode head, int n) {
    if (head.next == null && n == 1) return null;
    ListNode node = head;

    //calculate the size of head linked list
    int size = 0;
    while (node != null) {
      size++;
      node = node.next;
    }

    //if n = size then remove the first element from linked list (return the second reference to linked list)
    if (size == n) return head.next;

    //reset the node to head reference, pass through the linked list till reaching the n'th+1 node from the end.
    //Remove the n'th node from the end.
    node = head;
    while (size > n+1) {
      node = node.next;
      size--;
    }
    if (node.next.next != null) node.next = node.next.next;
    else node.next = null;

    return head;
  }
}
