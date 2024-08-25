//{ Driver Code Starts


import java.io.*;
import java.lang.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static PrintWriter ot;

    public static void main(String args[]) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        ot = new PrintWriter(System.out);
        int t = Integer.parseInt(br.readLine().trim());
        while (t-- > 0) {
            String s[] = br.readLine().trim().split(" ");
            int V = Integer.parseInt(s[0]);
            int E = Integer.parseInt(s[1]);
            List<List<int[]>> list = new ArrayList<>();
            for (int i = 0; i < V; i++) list.add(new ArrayList<>());
            for (int i = 0; i < E; i++) {
                s = br.readLine().trim().split(" ");
                int a = Integer.parseInt(s[0]);
                int b = Integer.parseInt(s[1]);
                int c = Integer.parseInt(s[2]);
                list.get(a).add(new int[] {b, c});
                list.get(b).add(new int[] {a, c});
            }
            ot.println(new Solution().spanningTree(V, E, list));
        }
        ot.close();
    }
}
// } Driver Code Ends

class Tuple implements Comparable<Tuple> {
    int wt, curr, parent;
    
    public Tuple (int wt, int curr, int parent) {
        this.wt = wt;
        this.curr = curr;
        this.parent = parent;
    }
    
    @Override
    public int compareTo(Tuple other) {
        if (this.wt != other.wt)
            return Integer.compare(this.wt, other.wt);
        return Integer.compare(this.curr, other.curr);
    }
}

// User function Template for Java

class Solution {
    static int spanningTree(int V, int E, List<List<int[]>> adj) {
        // Code Here.
        int sum = 0;
        PriorityQueue<Tuple> pq = new PriorityQueue<>();
        pq.offer(new Tuple(0, 0, -1));
        boolean[] vis = new boolean[V];
        while (!pq.isEmpty()) {
            Tuple currNode = pq.poll();
            if (currNode.parent != -1) {
                if (vis[currNode.curr] == false) {
                    sum += currNode.wt;
                    vis[currNode.curr] = true;
                }
                else
                    continue;
            }
            else
                vis[currNode.curr] = true;
            // [[(1,5), (2,1)], [(0,5), (2,3)], [(0,1), (1,3)]]
            List<int[]> neighs = adj.get(currNode.curr);
            for (int[] neigh: neighs) {
                if (vis[neigh[0]] == false) {
                    pq.offer(new Tuple(neigh[1], neigh[0], currNode.curr));
                }
            }
        }
        return sum;
    }
}