package LeetCodeAlgorithms;
import java.util.Stack;

/**
 * Created by dianaluca on 10/5/16.
 */

public class ImplementQueueUsingStacks {
  class MyQueue {
    Stack<Integer> oldStack = new Stack<>();
    Stack<Integer> newStack = new Stack<>();

    private void moveNewToOldStack() {
      while(!newStack.empty())
        oldStack.push(newStack.pop());
    }

    // Push element x to the back of queue. O(1)
    public void push(int x) {
      newStack.push(x);
    }

    // Removes the element from in front of queue. O(N)
    public void pop() {
      if(oldStack.empty()) moveNewToOldStack();
      oldStack.pop();
    }

    // Get the front element.
    public int peek() {
      if (oldStack.empty()) {
        moveNewToOldStack();
      }
      return oldStack.peek();
    }

    // Return whether the queue is empty.
    public boolean empty() {
      if (oldStack.empty() && newStack.empty()) return true;
      else return false;
    }
  }
}
