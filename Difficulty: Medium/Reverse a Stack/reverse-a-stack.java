//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.io.*;
import java.lang.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        PrintWriter out=new PrintWriter(System.out);
        
        //taking testcases
        int t = Integer.parseInt(br.readLine()); 
    	for(int i=0;i<t;i++)
    	{
            String str=br.readLine();
    		
    		//input n and d
    	    int n=Integer.parseInt(str);
    		Stack<Integer> stack=new Stack<>();
    		String str1=br.readLine();
    		String[] starr1=str1.split(" ");
    		//inserting elements in the array
    		for(int j=0;j<n;j++)
    		{
    		    stack.push(Integer.parseInt(starr1[j]));
    		}
    		//calling reverse() function
            Solution.reverse(stack);
            for(int j:stack){
                out.print(j+" ");
            }
            out.println();
         }
         out.close();
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution
{ 
    static void insert(int temp, Stack<Integer> s) {
        if (s.isEmpty()) {
            s.push(temp);
            return;
        }
        int t = s.pop();
        insert(temp, s);
        s.push(t);
    }
    
    static void reverseStk(Stack<Integer> s) {
        if (s.isEmpty())
            return;
        int temp = s.pop();
        reverseStk(s);
        insert(temp, s);
    }
    
    static void reverse(Stack<Integer> s)
    {
        // add your code here
        reverseStk(s);
    }
}