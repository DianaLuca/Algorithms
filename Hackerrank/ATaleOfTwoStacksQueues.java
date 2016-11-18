package Algorithms.Hackerrank;
import java.util.*;

/**
 * In this challenge, you must first implement a queue using two stacks.
 * Then process q queries, where each query is one of the following 3 types:
 *
 * 1) 1 x: Enqueue element x into the end of the queue.
 * 2) 2: Dequeue the element at the front of the queue.
 * 3) 3: Print the element at the front of the queue.

 * Created by dianaluca on 11/18/16.
 */

public class ATaleOfTwoStacksQueues {

  public static class MyQueue<T> {
    Stack<T> stackNewestOnTop = new Stack<T>();
    Stack<T> stackOldestOnTop = new Stack<T>();

    public void enqueue(T value) { // Push onto newest stack
      stackNewestOnTop.push(value);
    }

    public T peek() {
      if (stackOldestOnTop.isEmpty()) moveNewToOld(stackNewestOnTop, stackOldestOnTop);
      return stackOldestOnTop.peek();
    }

    public T dequeue() {
      if (stackOldestOnTop.isEmpty()) moveNewToOld(stackNewestOnTop, stackOldestOnTop);
      return stackOldestOnTop.pop();
    }

    public void moveNewToOld(Stack<T> stackNewestOnTop, Stack<T> stackOldestOnTop) {
      while (!stackNewestOnTop.isEmpty()) stackOldestOnTop.push(stackNewestOnTop.pop());
    }
  }

  /**
   * Sample Input

   10       -the number of queries
   1 42     -type1 = put(value = 42)
   2        -type2 = pop()
   1 14     -type1 = put(value = 14)
   3        -type3 = peek()
   1 28     - .. put(28)
   3        - .. peek()
   1 60     - .. put(60)
   1 78     - .. put(78)
   2        - .. pop()
   2        - .. pop()

   Sample Output :
   For each query of type 3 ( peek() ), print the value of the element at the front of the queue on a new line.

   14
   14

   */
  public static void main(String[] args) {
    MyQueue<Integer> queue = new MyQueue<Integer>();

    Scanner scan = new Scanner(System.in);
    int n = scan.nextInt();

    for (int i = 0; i < n; i++) {
      int operation = scan.nextInt();
      if (operation == 1) { // enqueue
        queue.enqueue(scan.nextInt());
      } else if (operation == 2) { // dequeue
        queue.dequeue();
      } else if (operation == 3) { // print/peek
        System.out.println(queue.peek());
      }
    }
    scan.close();
  }
}
