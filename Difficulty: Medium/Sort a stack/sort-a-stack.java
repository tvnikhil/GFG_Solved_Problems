//{ Driver Code Starts
import java.util.*;
import java.util.Scanner;
import java.util.Stack;

class SortedStack {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            Stack<Integer> s = new Stack<>();
            int n = sc.nextInt();
            while (n-- > 0) s.push(sc.nextInt());
            GfG g = new GfG();
            Stack<Integer> a = g.sort(s);
            while (!a.empty()) {
                System.out.print(a.peek() + " ");
                a.pop();
            }
            System.out.println();
        }
    }
}
// } Driver Code Ends


/*Complete the function below*/
class GfG {
    void insert(int t, Stack<Integer> s) {
        if (s.isEmpty()) {
            s.push(t);
            return;
        }
        if (s.peek() > t) {
            int temp = s.pop();
            insert(t, s);
            s.push(temp);
        }
        else {
            s.push(t);
        }
    }
    
    void helper(Stack<Integer> s) {
        if (s.isEmpty())
            return;
        int t = s.pop();
        helper(s);
        insert(t, s);
    }
    
    public Stack<Integer> sort(Stack<Integer> s) {
        // add code here.
        helper(s);
        return s;
    }
}