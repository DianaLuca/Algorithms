package Algorithms.Hackerrank;
import java.util.*;

/**
 * Tries = a type of a tree which store characters
 * We're going to make our own Contacts application!
 * The application must perform two types of operations:
 *
 * -> 'add name' , where name is a string denoting a contact name.
 * This must store name as a new contact in the application
 *
 * -> 'find partial' , where partial is a string denoting a partial name to search the application for.
 * It must count the number of contacts starting with partial and print the count on a new line.
 *
 * Given n sequential add and find operations, perform each operation in order.

 * Created by dianaluca on 11/20/16.
 */
public class ContactsTries {

  static class TrieNode {
    // No. of contacts possible after reaching this node in the trie
    int noOfContacts = 0;
    // Next characters in the 26-array trie
    TrieNode[] children = new TrieNode[26];

    void add(String s) {
      TrieNode current = this; // Begin with the current node and start adding each character

      for (int i = 0; i < s.length(); i++) {
        int index = s.charAt(i) - 'a';

        if (current.children[index] == null) {
          current.children[index] = new TrieNode();
        }
        current.noOfContacts++;
        current = current.children[index];
      }

      current.noOfContacts++; // Leaf node should have count 1
    }

    int search(String val) {
      TrieNode current = this; // Begin search from the current node

      for(int i = 0; i < val.length(); i++) {
        int index = val.charAt(i) - 'a';
        current = current.children[index];

        if(current == null) {
          break;
        }
      }
      return (current == null)? 0 : current.noOfContacts;
    }
  }

  /**
   *
   Sample Input
   4      -> n = 4
   add hack
   add hackerrank
   find hac
   find hak

   Sample Output
   2
   0

   */

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    TrieNode root = new TrieNode();

    for(int a0 = 0; a0 < n; a0++) {
      String op = in.next();
      String contact = in.next();

      if(op.equals("add")) {
        root.add(contact);
      } else {
        System.out.println(root.search(contact));
      }
    }
  }
}
