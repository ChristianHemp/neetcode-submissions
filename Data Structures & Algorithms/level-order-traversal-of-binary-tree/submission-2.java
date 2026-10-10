class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Deque<TreeNode> queue = new ArrayDeque<>();
        List<List<Integer>> result = new ArrayList<List<Integer>>();

        if (root == null) {
            return result;
        }

        queue.addLast(root);
        int level = 0;
        while (!queue.isEmpty()) {
            result.add(new ArrayList<Integer>());
            int curr_length = queue.size();

            for (int i = 0; i < curr_length; i++) {
                TreeNode curr_node = queue.pollFirst();
                result.get(level).add(curr_node.val);
                
                if (curr_node.left != null) {
                    queue.addLast(curr_node.left);
                }
                if (curr_node.right != null) {
                    queue.addLast(curr_node.right);
                }
            }

            level++;
        }
        return result;
    }
}