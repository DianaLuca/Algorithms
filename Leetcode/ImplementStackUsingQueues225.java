package Algorithms.Leetcode;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by dianaluca on 10/5/16.
 */

public class ImplementStackUsingQueues225 {

  /**
   * Method 1:
   * push() - O(1)
   * pop() - O(N)
   * 2(two) Queues
   */
  public class StackWithTwoQ {
    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();
    int top;

    public void push(int x) {
      q1.add(x);
      top = x;
    }

    public void pop() {
      while(q1.size() > 1) {
        top = q1.poll();
        q2.add(top);
      }
      q1.poll();

      Queue<Integer> tmp = q1; //empty
      q1 = q2;
      q2 = tmp; //empty
    }

    public int top() {
      return top;
    }

    public boolean empty() {
      return q1.size() == 0;
    }
  }

  /**
   * Method 2:
   * push() - O(1)
   * pop() - O(N)
   * 1(one) Queue
  */
   public class StackWithOneQ {
    Queue<Integer> q1 = new LinkedList<>();
    int top;

    public void push(int x) {
      q1.add(x);
      top = x;
    }

    public void pop() {
      int N = q1.size();

      while(N > 1) {
        top = q1.poll();
        q1.add(top);
        N--;
      }

      q1.poll();
    }

    public int top() {
      return top;
    }

    public boolean empty() {
      return q1.size() == 0;
    }
  }

  /**
   * Method 3:
   * push() - O(N)
   * pop() - O(1)
   * 2(two) Queues
   */
  public class StackWithQueues {
    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();
    Queue<Integer> tmp;

    public void push(int x) {
      q2.add (x);

      while(!q1.isEmpty()) {
        q2.add(q1.poll());
      }

      tmp = q1;
      q1 = q2;
      q2 = tmp;
    }

    public void pop() {
      q1.poll();
    }

    public int top() {
      return q1.peek();
    }

    public boolean empty() {
      return q1.size() == 0;
    }
  }
}
