package LeetCodeAlgorithms;

/**
 * Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
 * According to the definition of LCA on Wikipedia:
 * “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that
 * has both v and w as descendants (where we allow a node to be a descendant of itself).”
 *
 * Created by dianaluca on 9/23/16.
 */

public class LowestCommonAncestorBST235 {

  public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
  }

  public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    if (root == null) return null;
    if (p.val == root.val || q.val == root.val) return root;

    if(p.val < q.val) { //p.val < q.val
      if (q.val > root.val && p.val < root.val) return root;
      else if (q.val < root.val ) return lowestCommonAncestor(root.left, p, q);
      else return lowestCommonAncestor(root.right, p, q);
    } else {  //p.val > q.val
      if (p.val > root.val && q.val < root.val) return root;
      else if (p.val < root.val) return lowestCommonAncestor(root.left, p, q);
      else return lowestCommonAncestor(root.right, p, q);
    }
  }
}
