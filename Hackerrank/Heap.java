package Algorithms.Hackerrank;
import java.util.*;

/**
 * Created by dianaluca on 11/21/16.
 */

public abstract class Heap {
  protected int capacity; //current array length
  protected int size;  //current nr of elements in heap
  protected int[] items;

  public Heap() {
    this.capacity = 10;
    this.size = 0;
    this.items = new int[capacity];
  }

  /**
   * @param parentIndex The index of the parent element.
   * @return The index of the left child.
   */
  public int getLeftChildrenIndex(int parentIndex) {
    return 2 * parentIndex + 1;
  }

  public int getRightChildrenIndex(int parentIndex) {
    return 2 * parentIndex + 2;
  }

  public int getParentIndex(int childIndex) {
    return (childIndex - 1) / 2;
  }

  public boolean hasLeftChild(int index) {
    return getLeftChildrenIndex(index) < size;
  }

  public boolean hasRightChild(int index) {
    return getRightChildrenIndex(index) < size;
  }

  public boolean hasParent(int index) {
    return getParentIndex(index) >= 0;
  }

  public int leftChild(int index) {
    return items[getLeftChildrenIndex(index)];
  }

  public int rightChild(int index) {
    return items[getRightChildrenIndex(index)];
  }

  public int parent(int index) {
    return items[getParentIndex(index)];
  }

  public void swap(int indexOne, int indexTwo) {
    int tmp = items[indexOne];
    items[indexOne] = items[indexTwo];
    items[indexTwo] = tmp;
  }

  public void ensureCapacity() {
    if (capacity == size) {
      capacity = capacity << 1; // capacity^2
      items = Arrays.copyOf(items, capacity);
    }
  }

  public int peek() {
    isEmpty("peek");
    return items[0];
  }

  /**
   * Throws IllegalStateException if Heap is empty
   * @param methodName
   */
  public void isEmpty(String methodName) {
    if (size == 0) {
      throw new IllegalStateException(
          "You cannot perform '" + methodName + "' on an empty Heap."
      );
    }
  }

  /**
   * Extract root element from heap
   */
  public int poll() {
    //Throws exception if Heap is empty
    isEmpty("poll");

    //Heap is not empty
    int item = items[0];
    items[0] = items[size - 1];
    size--;
    heapifyDown();
    return item;
  }

  public void add(int item) {
    ensureCapacity();

    items[size] = item;
    size++;

    heapifyUp();
  }

  /** Swap values down the Heap. **/
  public abstract void heapifyDown();

  /** Swap values up the Heap. **/
  public abstract void heapifyUp();
}

class MaxHeap extends Heap {

  public void heapifyDown() {
    int index = 0;

    while (hasLeftChild(index)) {
      int smallerChildIndex = getLeftChildrenIndex(index);

      if (hasRightChild(index) && rightChild(index) > leftChild(index)) {
        smallerChildIndex = getRightChildrenIndex(index);
      }

      if(items[index] > items[smallerChildIndex]) {
        break;
      } else {
        swap(index, smallerChildIndex);
      }

      index = smallerChildIndex;
    }
  }

  public void heapifyUp() {
    int index = size - 1;

    while (hasParent(index) && parent(index) < items[index]) {
      swap(getParentIndex(index), index);
      index = getParentIndex(index);
    }
  }
}

class MinHeap extends Heap {

  public void heapifyDown() {
    int index = 0;

    while (hasLeftChild(index)) {
      int smallerChildIndex = getLeftChildrenIndex(index);

      if (hasRightChild(index) && rightChild(index) < leftChild(index)) {
        smallerChildIndex = getRightChildrenIndex(index);
      }

      if (items[index] < items[smallerChildIndex]) {
        break;
      } else {
        swap(index, smallerChildIndex);
      }

      index = smallerChildIndex;
    }
  }

  public void heapifyUp() {
    int index = size - 1;

    while (hasParent(index) && parent(index) > items[index]) {
      swap(getParentIndex(index), index);
      index = getParentIndex(index);
    }
  }


  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int range = scanner.nextInt();
    scanner.close();

    // Insert random values into heaps:
    Heap minHeap = new MinHeap();
    Heap maxHeap = new MaxHeap();
    System.out.println("Insert Number Sequence:");
    for(int i = 0; i < range; i++) {
      int value = (int) (Math.random() * 100);
      minHeap.add(value);
      maxHeap.add(value);
      System.out.print(+ value + " ");
    }

    // Remove values from heaps:
    System.out.println("\n\nPoll Values:\n------------\nMinHeap MaxHeap");
    for(int i = 0; i < range; i++) {
      System.out.format("  %-12d", minHeap.poll());
      System.out.format("%-6d\n", maxHeap.poll());
    }
    try {
      minHeap.peek();
    }
    catch(IllegalStateException e) {
      System.out.println(e.getMessage());
    }
    try {
      maxHeap.poll();
    }
    catch(IllegalStateException e) {
      System.out.println(e.getMessage());
    }
  }
}
