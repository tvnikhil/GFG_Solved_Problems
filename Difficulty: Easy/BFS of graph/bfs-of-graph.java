//{ Driver Code Starts
// Initial Template for Java
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while (T-- > 0) {
            String[] s = br.readLine().trim().split(" ");
            int V = Integer.parseInt(s[0]);
            int E = Integer.parseInt(s[1]);
            ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
            for (int i = 0; i < V; i++) adj.add(i, new ArrayList<Integer>());
            for (int i = 0; i < E; i++) {
                String[] S = br.readLine().trim().split(" ");
                int u = Integer.parseInt(S[0]);
                int v = Integer.parseInt(S[1]);
                adj.get(u).add(v);
                // adj.get(v).add(u);
            }
            Solution obj = new Solution();
            ArrayList<Integer> ans = obj.bfsOfGraph(V, adj);
            for (int i = 0; i < ans.size(); i++)
                System.out.print(ans.get(i) + " ");
            System.out.println();
        }
    }
}

// } Driver Code Ends


class Solution {
    // Function to return Breadth First Traversal of given graph.
    static void bfs(int src, ArrayList<ArrayList<Integer>> adj,
                    Queue<Integer> que, boolean[] visited, ArrayList<Integer> ans) {
        que.offer(src);
        visited[src] = true;
        while (!que.isEmpty()) {
            int qSize = que.size();
            for (int j = 0; j < qSize; j++) {
                src = que.poll();
                ans.add(src);
                ArrayList<Integer> vertices = adj.get(src);
                for (int i = 0; i < vertices.size(); i++) {
                    int vertex = vertices.get(i);
                    if (visited[vertex] == false) {
                        que.offer(vertex);
                        visited[vertex] = true;
                    }
                }
            }
        }
    }
    
    
    public ArrayList<Integer> bfsOfGraph(int V, ArrayList<ArrayList<Integer>> adj) {
        // Code here
        boolean[] visited = new boolean[V];
        Queue<Integer> que = new LinkedList<>();
        ArrayList<Integer> ans = new ArrayList<>();
        bfs(0, adj, que, visited, ans);
        return ans;
    }
}