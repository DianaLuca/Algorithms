package Algorithms.Hackerrank;
import java.util.*;

/**
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

public class ContactsAppWithHashMap {

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
    HashMap<Character, ArrayList<String>> hm = new HashMap<Character, ArrayList<String>>();

    for(int a0 = 0; a0 < n; a0++){
      String op = in.next();
      String contact = in.next();

      if (op.equals("add")) {
        if (hm.containsKey(contact.charAt(0))) {
          ArrayList<String> arr = hm.get(contact.charAt(0));
          arr.add(contact);
          hm.put(contact.charAt(0),arr);
        } else {
          ArrayList<String> arr = new ArrayList<String>();
          arr.add(contact);
          hm.put(contact.charAt(0), arr);
        }
      } else {   // "find partial"
        if (!hm.containsKey(contact.charAt(0))) System.out.println(0);
        else findAndPrint(hm.get(contact.charAt(0)), contact);
      }
    }
  }

  public static void findAndPrint(ArrayList<String> arr, String contact) {
    int N = contact.length();
    int res = 0;

    for (String name : arr) {
      if (name.length() >= contact.length()) {
        String tmpStr = name.substring(0, N);
        if (tmpStr.equals(contact)) res++;
      }
    }

    System.out.println(res);
  }
}
