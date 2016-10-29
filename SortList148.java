package LeetCodeAlgorithms;

import java.util.ArrayList;
import java.util.Arrays;

/**
 * Sort a linked list in O(n log n) time using constant space complexity.
 *
 * Created by dianaluca on 10/27/16.
 */

public class SortList148 {

  public static int cnt = 0;
  public static class ListNode {
      int val;
      ListNode next;
      ListNode(int x) { val = x; }
    }

  /**
   * Solution 1: Merge-Sort
   * O(n log n) time using constant space complexity.
   */
  public static ListNode sortList(ListNode head) {
    if(head == null || head.next == null) return head;

    //count iteration number
    cnt++;
    System.out.print("\ncnt = " + cnt + "\n ");

    // step 1. cut the list to two halves
    ListNode prev = null, slow = head, fast = head;

    while (fast != null && fast.next != null) {
      prev = slow;
      slow = slow.next;
      fast = fast.next.next;
      if (fast != null) System.out.printf("\nprev= %d, slow= %d, fast= %d ",prev.val,slow.val,fast.val);
      if (fast == null) System.out.printf("\nprev= %d, slow= %d",prev.val,slow.val);
    }

    System.out.println("\nHead before prev:");
    ListNode tmp = head;
    while(tmp != null) {
      System.out.print(tmp.val + ", ");
      tmp = tmp.next;
    }

    prev.next = null;

    System.out.println("\nHead after prev:");
    ListNode tmp2 = head;
    while(tmp2 != null) {
      System.out.print(tmp2.val + ", ");
      tmp2 = tmp2.next;
    }
    // step 2. sort each half
    ListNode l1 = sortList(head);
    ListNode l2 = sortList(slow);

    // step 3. merge l1 and l2
    return merge(l1, l2);
  }

  public static ListNode merge(ListNode A, ListNode B) {
    if (A == null) return B;
    if (B == null) return A;

    if (A.val < B.val) {
      A.next = merge(A.next, B);
      return A;
    } else {
      B.next = merge(A, B.next);
      return B;
    }
  }

  /**
   * Solution 2: with arrayList
   * O(n log n) time using O(n) space complexity.
   */
  public ListNode sortList2(ListNode head) {
    if(head == null || head.next == null) return head;
    ArrayList<Integer> vals = new ArrayList<Integer>();
    ListNode node = head;
    while (node != null) {
      Integer val = node.val;
      vals.add(val);
      node = node.next;
    }

    //transform arrayList "vals" to a list "list" and sort it O(N*logN)-quicksort(pivot)
    Integer[] list = vals.toArray(new Integer[vals.size()]);
    Arrays.sort(list);

    head = new ListNode(0);
    node = head;
    for (int i = 0; i < list.length; i++) {
      node.val = list[i];
      if (i != list.length - 1) {
        node.next = new ListNode(0);
        node = node.next;
      }
    }
    return head;
  }

  //test client
  public static void main(String[] args) {
    ListNode head = new ListNode(8);
    head.next = new ListNode(7);
    head.next.next = new ListNode(6);
    head.next.next.next = new ListNode(5);
    head.next.next.next.next = new ListNode(4);
    head.next.next.next.next.next = new ListNode(3);
    head.next.next.next.next.next.next = new ListNode(2);
    head.next.next.next.next.next.next.next = new ListNode(1);

    ListNode res = sortList(head);
    System.out.println("\nAfter mergesort:");
    while(res != null) {
      System.out.print(res.val + ", ");
      res = res.next;
    }
  }
}
