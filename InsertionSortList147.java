package LeetCodeAlgorithms;

/**
 * Sort a linked list using insertion sort.
 *
 * Created by dianaluca on 10/29/16.
 */

public class InsertionSortList147 {
  public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
  }

  public ListNode insertionSortList(ListNode node) {
    ListNode sortedList = null;
    while(node != null) {
      ListNode current = node; //1,1
      node = node.next; //1
      ListNode x;
      ListNode previous = null;
      for (x = sortedList; x != null; x = x.next) {
        if (current.val < x.val) {
          break;
        }
        previous = x;
      }

      if (previous == null) {
        current.next = sortedList;
        sortedList = current;
      } else {
        current.next = previous.next;
        previous.next = current;
      }
    }
    return sortedList;
  }
}
