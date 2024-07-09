//{ Driver Code Starts
import java.io.*;
import java.util.*;


class IntArray
{
    public static int[] input(BufferedReader br, int n) throws IOException
    {
        String[] s = br.readLine().trim().split(" ");
        int[] a = new int[n];
        for(int i = 0; i < n; i++)
            a[i] = Integer.parseInt(s[i]);
        
        return a;
    }
    
    public static void print(int[] a)
    {
        for(int e : a)
            System.out.print(e + " ");
        System.out.println();
    }
    
    public static void print(ArrayList<Integer> a)
    {
        for(int e : a)
            System.out.print(e + " ");
        System.out.println();
    }
}


class IntMatrix
{
    public static int[][] input(BufferedReader br, int n, int m) throws IOException
    {
        int[][] mat = new int[n][];
        
        for(int i = 0; i < n; i++)
        {
            String[] s = br.readLine().trim().split(" ");
            mat[i] = new int[s.length];
            for(int j = 0; j < s.length; j++)
                mat[i][j] = Integer.parseInt(s[j]);
        }
        
        return mat;
    }
    
    public static void print(int[][] m)
    {
        for(var a : m)
        {
            for(int e : a)
                System.out.print(e + " ");
            System.out.println();
        }
    }
    
    public static void print(ArrayList<ArrayList<Integer>> m)
    {
        for(var a : m)
        {
            for(int e : a)
                System.out.print(e + " ");
            System.out.println();
        }
    }
}

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while(t-- > 0){
            
            int[] a = IntArray.input(br, 2);
            
            
            int[][] grid = IntMatrix.input(br, a[0], a[1]);
            
            Solution obj = new Solution();
            ArrayList<ArrayList<Integer>> res = obj.findAllPossiblePaths(a[0],a[1], grid);
            
            IntMatrix.print(res);
            
        }
    }
}

// } Driver Code Ends


class Solution {
    static void generate(int x, int y, int n, int m, int[][] grid,
                        ArrayList<Integer> currPath, 
                        ArrayList<ArrayList<Integer>> ans) {
        if ((x < 0 || x >= n) || (y < 0 || y >= m))
            return;
        if (x == n-1 && y == m-1) {
            currPath.add(grid[x][y]);
            ans.add(new ArrayList<>(currPath));
            currPath.remove(currPath.size()-1);
            return;
        }
        if (grid[x][y] == -1)
            return;
        currPath.add(grid[x][y]);
        generate(x+1, y, n, m, grid, currPath, ans);
        generate(x, y+1, n, m, grid, currPath, ans);
        currPath.remove(currPath.size()-1);
    }
    
    public static ArrayList<ArrayList<Integer>> findAllPossiblePaths(int n,int m, int[][] grid) {
        // code here
        ArrayList<ArrayList<Integer>> ans = new ArrayList<>();
        ArrayList<Integer> currPath = new ArrayList<>();
        generate(0, 0, n, m, grid, currPath, ans);
        return ans;
    }
}
        
