package LeetCodeAlgorithms;

import java.util.Stack;

/**
 * Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. All O(1)
 * push(x) -- Push element x onto stack.
 * pop() -- Removes the element on top of the stack.
 * top() -- Get the top element.
 * getMin() -- Retrieve the minimum element in the stack.
 *
 * Created by dianaluca on 10/6/16.
 */


public class MinStack155 {
  Stack<Integer> stack = new Stack<>();
  int min = Integer.MAX_VALUE;  // 2147483647

  public void push(int x) {
    if (x <= min) {
      stack.push(min);
      min = x;
      stack.push(x);
    } else {
      stack.push(x);
    }
  }

  public void pop() {
    if (stack.peek() == min) {
      stack.pop();
      min = stack.peek();
      stack.pop();
    } else {
      stack.pop();
    }
    if (stack.empty()) {
      min = Integer.MAX_VALUE;
    }

  }

  public int top() {
    return stack.peek();
  }

  public int getMin() {
    return min;
  }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */

