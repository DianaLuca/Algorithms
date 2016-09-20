package LeetCode;

/**
 * Given a sorted linked list, delete all duplicates such that each element appear only once.

 For example,
 Given 1->1->2, return 1->2.
 Given 1->1->2->3->3, return 1->2->3.

 * Created by dianaluca on 9/19/16.
 */

public class RemoveDuplicatesFromSortedList83 {
  /**
   * Definition for singly-linked list.
   */

  public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
  }

  public ListNode deleteDuplicatesIterative(ListNode head) {
    if(head == null || head.next == null) return head;
    ListNode currentNode = head;
    while (head.next != null) {
      if(head.next.val == head.val) {
        head.next = head.next.next;
      }
      else head = head.next;
    }
    return currentNode;
  }

  public ListNode deleteDuplicatesRecursive(ListNode head) {
    if(head == null || head.next == null) return head;

    if(head.next.val == head.val) {
      head.next = head.next.next;
      head = deleteDuplicatesRecursive(head);
    }
    else head.next = deleteDuplicatesRecursive(head.next);

    return head;
  }
}
