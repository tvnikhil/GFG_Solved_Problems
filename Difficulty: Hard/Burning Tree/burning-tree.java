//{ Driver Code Starts
//Initial Template for Java


import java.util.LinkedList;
import java.util.Queue;
import java.io.*;
import java.util.*;

class Node {
	int data;
	Node left;
	Node right;

	Node(int data) {
		this.data = data;
		left = null;
		right = null;
	}
}

class GfG {

	static Node buildTree(String str) {

		if (str.length() == 0 || str.charAt(0) == 'N') {
			return null;
		}

		String ip[] = str.split(" ");
		// Create the root of the tree
		Node root = new Node(Integer.parseInt(ip[0]));
		// Push the root to the queue

		Queue<Node> queue = new LinkedList<>();

		queue.add(root);
		// Starting from the second element

		int i = 1;
		while (queue.size() > 0 && i < ip.length) {

			// Get and remove the front of the queue
			Node currNode = queue.peek();
			queue.remove();

			// Get the current node's value from the string
			String currVal = ip[i];

			// If the left child is not null
			if (!currVal.equals("N")) {

				// Create the left child for the current node
				currNode.left = new Node(Integer.parseInt(currVal));
				// Push it to the queue
				queue.add(currNode.left);
			}

			// For the right child
			i++;
			if (i >= ip.length)
				break;

			currVal = ip[i];

			// If the right child is not null
			if (!currVal.equals("N")) {

				// Create the right child for the current node
				currNode.right = new Node(Integer.parseInt(currVal));

				// Push it to the queue
				queue.add(currNode.right);
			}
			i++;
		}

		return root;
	}

	static void printInorder(Node root) {
		if (root == null)
			return;

		printInorder(root.left);
		System.out.print(root.data + " ");

		printInorder(root.right);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int t = Integer.parseInt(br.readLine());

		while (t > 0) {
			String s = br.readLine();
			int target = Integer.parseInt(br.readLine());
			Node root = buildTree(s);

			Solution g = new Solution();
			System.out.println(g.minTime(root, target));
			t--;

		}
	}
}



// } Driver Code Ends


//User function Template for Java

class Solution
{
    /*class Node {
    	int data;
    	Node left;
    	Node right;
    
    	Node(int data) {
    		this.data = data;
    		left = null;
    		right = null;
    	}
    }*/
    static void getParents(Node root, Map<Node, Node> childParent, Node[] src, int target) {
        if (root == null)
            return;
        if (root.data == target)
            src[0] = root;
        if (root.left != null)
            childParent.put(root.left, root);
        if (root.right != null)
            childParent.put(root.right, root);
        getParents(root.left, childParent, src, target);
        getParents(root.right, childParent, src, target);
    }
    
    static int dfs(Node src, int time, Map<Node, Node> childParent, Map<Node, Boolean> visited, int visitedCnt) {
        if (src == null)
            return time-1;
        if (visitedCnt == childParent.size())
            return time-1;
        if (visited.containsKey(src) == true)
            return time-1;
        visited.put(src, true);
        int max = -1;
        int x = dfs(src.left, time+1, childParent, visited, visitedCnt+1);
        max = Math.max(x, max);
        int y = dfs(src.right, time+1, childParent, visited, visitedCnt+1);
        max = Math.max(y, max);
        int z = dfs(childParent.get(src), time+1, childParent, visited, visitedCnt+1);
        max = Math.max(z, max);
        visited.remove(src);
        return max;
    }
    
    public static int minTime(Node root, int target) 
    {
        // Your code goes here
        Map<Node, Node> childParent = new HashMap<>();
        Node[] src = new Node[1];
        childParent.put(root, null);
        getParents(root, childParent, src, target);
        Map<Node, Boolean> visited = new HashMap<>();
        int visitedCnt = 0;
        int time = dfs(src[0], 0, childParent, visited, visitedCnt);
        return time;
    }
}