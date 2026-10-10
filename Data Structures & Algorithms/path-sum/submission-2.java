/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        return pathSumHelper(root, 0, targetSum);
    }

    private boolean pathSumHelper(TreeNode node, int currSum, int targetSum) {
        if (node == null) {
            return false;
        }

        currSum += node.val;

        if(node.left == null && node.right == null) {
            if(currSum == targetSum) {
                return true;
            } else {
                return false;
            }
        }

        if(pathSumHelper(node.left, currSum, targetSum)) {
            return true;
        }

        if(pathSumHelper(node.right, currSum, targetSum)) {
            return true;
        }

        return false;
    }
}