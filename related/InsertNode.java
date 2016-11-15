package Algorithms.related;

/**
 * You’re given the pointer to the head node of a linked list,
 * Sort the linked list using Insertion Sort Algorithm and return the head of
 * the sorted list.
 *
 * Created by dianaluca on 10/28/16.
 */

public class InsertNode {
  public static class Node {
    int val;
    Node next;
    Node(int x) {
      val = x;
      next = null;
    }
  }

  public static Node sortLinkedList(Node node) {
    //use Insertion Sort
    Node sortedList = null;
    while (node != null) {
      Node current = node; //10, 9, 5
      node = node.next; //9, 5
      Node x;
      Node previous = null;
      for ( x = sortedList; x != null; x = x.next){
        if (current.val < x.val){
          break;
        }
        previous = x;
      }
      if(previous == null){
        current.next = sortedList;
        sortedList = current;
      }
      else {
        current.next = previous.next;
        previous.next = current;
      }
    }
    return sortedList;
  }

  public static void main(String[] args) {
    Node head = new Node(10);
    head.next = new Node(9);
    head.next.next = new Node(5);
    head.next.next.next = new Node(1);
    head.next.next.next.next = new Node(1);
    head.next.next.next.next.next = new Node(2);

    Node test = head;
    while (test !=  null) {
      System.out.print(test.val + ", ");
      test = test.next;
    }

    System.out.print("\nSort the linked list\n");
    head = sortLinkedList(head); //7, 2, 9, 5
    Node testSort = head;
    while (testSort !=  null) {
      System.out.print(testSort.val + ", ");
      testSort = testSort.next;
    }
  }
}
