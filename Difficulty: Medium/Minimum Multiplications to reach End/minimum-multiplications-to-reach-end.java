//{ Driver Code Starts
// Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

// Position this line where user code will be pasted.

class GFG {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0) {
            int n = sc.nextInt();
            int[] a = new int[n];

            for (int i = 0; i < n; i++) {
                a[i] = sc.nextInt();
            }

            int start = sc.nextInt();
            int end = sc.nextInt();

            Solution ob = new Solution();
            int ans = ob.minimumMultiplications(a, start, end);
            System.out.println(ans);
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    int minimumMultiplications(int[] arr, int start, int end) {
        if (start == end) return 0;
        // Your code here
        int[] dist = new int[100000];
        int mod = 100000;
        for (int i = 0; i < 100000; i++) dist[i] = Integer.MAX_VALUE;
        Queue<Integer> pque = new LinkedList<>();
        pque.offer(start);
        dist[start] = 0;
        int level = 1;
        while (!pque.isEmpty()) {
            //System.out.println(level);
            int size = pque.size();
            for (int i = 0; i < size; i++) {
                int curr = pque.poll();
                //System.out.println("curr" + " " + curr);
                for (int j = 0; j < arr.length; j++) {
                    int mul = (curr * arr[j]) % mod;
                    //System.out.println(mul);
                    if (mul == end) return level;
                    if (dist[mul] == Integer.MAX_VALUE) {
                        dist[mul] = level;
                        pque.offer(mul);
                    }
                    // if (level < dist[mul]) {
                    //     dist[mul] = level;
                    //     pque.offer(mul);
                    // }
                }
            }
            level++;
        }
        return -1;
    }
}
