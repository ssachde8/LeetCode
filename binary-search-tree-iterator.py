/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 
public class BSTIterator {
	Stack<TreeNode> stack;
 
	public BSTIterator(TreeNode root) {
		stack = new Stack<TreeNode>();
		while (root != null) {
			stack.push(root);
			root = root.left;
		}
	}
 
	public boolean hasNext() {
		return !stack.isEmpty();
	}
 
	public int next() {
		TreeNode cur = stack.pop();
		int result = cur.val;
		if (cur.right != null) {
			cur = cur.right;
			while (cur != null) {
				stack.push(cur);
				cur = cur.left;
			}
		}
		return result;
	}
}