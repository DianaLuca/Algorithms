package Algorithms.Hackerrank;

/**
 * For the purposes of this challenge, we define a binary search tree to be a binary tree with the following ordering properties:
 * The data value of every node in a node's left subtree is less than the data value of that node.
 * The data value of every node in a node's right subtree is greater than the data value of that node.
 * Given the root node of a binary tree, can you determine if it's also a binary search tree?
 *
 * Created by dianaluca on 11/19/16.
 */

public class IsThisABinarySearchTree {
  //The Node class is defined as follows:
  class Node {
    int data;
    Node left;
    Node right;
  }

  boolean checkBST(Node root) {
    return isBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
  }

  boolean isBST(Node root, int min, int max) {
    if(root == null) return true;

    return (root.data > min && root.data < max &&
        isBST(root.left, min, root.data) &&
        isBST(root.right, root.data, max));
  }
}
