//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
import java.lang.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-- > 0){
            int n = Integer.parseInt(in.readLine());
            
            Solution ob = new Solution();
            ArrayList<Integer> ans = ob.recamanSequence(n);
            for(int i = 0;i < n;i++)
                System.out.print(ans.get(i)+" ");
            System.out.println();
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution{
    // static int helper(int n, ArrayList<Integer> l, Set<Integer> hs) {
    //     if (n == 0)
    //         return 0;
    //     int res = helper(n-1, l, hs);
    //     if (res - n > 0 && hs.contains(res-n) == false) res -= n;
    //     else res += n;
    //     l.set(n, res);
    //     hs.add(res);
    //     return l.get(n);
    // }
    
    static ArrayList<Integer> recamanSequence(int n){
        // code here
        ArrayList<Integer> l = new ArrayList<>(Collections.nCopies(n+1, 0));
        Set<Integer> hs = new HashSet<>();
        // helper(n, l, hs);
        for (int i = 0; i <= n; i++) {
            if (i == 0) {
                l.set(0, 0);
                hs.add(0);
            }
            else {
                int res = l.get(i-1);
                if (res - i > 0 && hs.contains(res-i) == false) {
                    l.set(i, res-i);
                    hs.add(res-i);
                }
                else {
                    l.set(i, res+i);
                    hs.add(res+i);
                }
            }
        }
        return l;
    }
}