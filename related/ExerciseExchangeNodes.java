package LeetCodeAlgorithms.related;


/**
 * Created by dianaluca on 9/25/16.
 */

public class ExerciseExchangeNodes {
  public static class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x;  }
  }

  public static void main(String[] args) {
    ListNode head = new ListNode(1);
    head.next = new ListNode(2);
    head.next.next = new ListNode(3);
    head.next.next.next = new ListNode(4);

    ListNode node = head;
    System.out.println("head before:");
     while  (node != null) {
       System.out.print(node.val + " ");
       node = node.next;
     }

    System.out.print("\n ---------- After exchanging nodes ------------ ");

    ListNode tmp = head.next;
    head.next = tmp.next;
    tmp.next = head;
    //head = tmp;

    System.out.println("\nhead:");
    int cnt = 0;
    while (head != null && cnt < 10) {
      System.out.print( head.val + " ");
      head = head.next;
      cnt++;
    }

    System.out.println("\ntmp:");
    int cnt2 = 0;
    while (tmp != null && cnt2 < 10) {
      System.out.print( tmp.val + " ");
      tmp = tmp.next;
      cnt2++;
    }

  }
}
