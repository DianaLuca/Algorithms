package LeetCodeAlgorithms;

/**
 * Created by dianaluca on 9/24/16.
 */
public class MergeTwoSortedLists21 {

  public static class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
  }

  public static ListNode mergeTwoListsRecursive(ListNode l1, ListNode l2) {
    if (l1 == null) return l2;
    if (l2 == null) return l1;
    //System.out.println("l1: " + l1.val + ", l2: " + l2.val);
    if (l1.val < l2.val) {
      l1.next = mergeTwoListsRecursive(l1.next, l2);
      //System.out.println("l1: " + l1.val);
      return l1;
    } else {
      l2.next = mergeTwoListsRecursive(l1, l2.next);
      //System.out.println("l2: " + l2.val);
      return l2;
    }
  }

  public static ListNode mergeTwoListsIterative(ListNode l1, ListNode l2) {
    ListNode answ = new ListNode(0);
    ListNode prev = answ;

    while (l1 != null && l2 != null) {
      if (l1.val  < l2.val) {
        prev.next = l1;
        l1 = l1.next;
      } else {
        prev.next = l2;
        l2 = l2.next;
      }
      prev = prev.next;
    }

    if (l2 == null) {
      prev.next = l1;
    } else  {
      prev.next = l2;
    }

    return answ.next;
  }


  // Test Client
  public static void main(String[] args) {
    ListNode l1 = new ListNode(1);
    l1.next = new ListNode(2);
    l1.next.next = new ListNode(5);

    ListNode l2 = new ListNode(3);
    l2.next = new ListNode(6);

//    ListNode mrg = mergeTwoListsRecursive(l1, l2);
    ListNode mrg = mergeTwoListsIterative(l1, l2);

    while (mrg != null) {
      System.out.print(mrg.val + " ");
      mrg = mrg.next;
    }
  }
}
