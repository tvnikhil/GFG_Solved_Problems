//{ Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int tc = scan.nextInt();

        while (tc-- > 0) {
            int N = scan.nextInt();
            int M = scan.nextInt();
            int E = scan.nextInt();

            boolean graph[][] = new boolean[N][N];

            for (int i = 0; i < E; i++) {
                int u = scan.nextInt() - 1;
                int v = scan.nextInt() - 1;
                graph[u][v] = true;
                graph[v][u] = true;
            }

            System.out.println(new solve().graphColoring(graph, M, N) ? 1 : 0);
        }
    }
}

// } Driver Code Ends


class solve {
    // Function to determine if graph can be coloured with at most M colours
    // such
    // that no two adjacent vertices of graph are coloured with same colour.
    boolean check(int src, int color, int[] colors, boolean[][] graph) {
        for (int i = 0; i < graph[src].length; i++) {
            if (graph[src][i] == true && colors[i] == color)
                return false;
        }
        return true;
    }
    
    boolean dfs(int src, boolean[][] graph, int[] colors, int m) {
        if (src >= graph.length) return true;
        for (int c = 1; c <= m; c++) {
            if (check(src, c, colors, graph)) {
                colors[src] = c;
                if (dfs(src+1, graph, colors, m))
                    return true;
                colors[src] = 0;
            }
        }
        return false;
    }
    
    public boolean graphColoring(boolean graph[][], int m, int n) {
        // Your code here
        int[] colors = new int[n];
        return dfs(0, graph, colors, m);
    }
}