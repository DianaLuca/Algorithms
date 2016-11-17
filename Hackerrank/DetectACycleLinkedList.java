package Algorithms.Hackerrank;
import java.util.*;
/**
 * A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
 *
 * Created by dianaluca on 11/17/16.
 */

public class DetectACycleLinkedList {
  /**
   *
   A Node is defined as:
   */
  class Node {
    int data;
    Node next;
  }

  boolean hasCycle(Node head) {
    // Complete this function
    // Do not write the main method
    if(head == null || head.next == null) return false;
    HashSet<Node> hs = new HashSet<>();

    while(!hs.contains(head)) {
      hs.add(head);
      head = head.next;

      if (head == null) return false;
    }

    return true;
  }
}
