//{ Driver Code Starts
import java.io.*;
import java.util.*;
import java.util.Scanner;

class Node {
    int data;
    Node next;
    Node bottom;

    Node(int d) {
        data = d;
        next = null;
        bottom = null;
    }
}

class Flatttening_A_LinkedList {
    Node head;

    void printList(Node node) {
        // Node temp = head;
        while (node != null) {
            System.out.print(node.data + " ");
            node = node.bottom;
        }
        System.out.println();
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        Flatttening_A_LinkedList list = new Flatttening_A_LinkedList();
        while (t > 0) {
            int N = sc.nextInt();
            int arr[] = new int[N];
            for (int i = 0; i < N; i++) arr[i] = sc.nextInt();

            Node temp = null;
            Node tempB = null;
            Node pre = null;
            Node preB = null;
            int flag = 1;
            int flag1 = 1;
            for (int i = 0; i < N; i++) {
                int m = arr[i];
                m--;
                int a1 = sc.nextInt();
                temp = new Node(a1);
                if (flag == 1) {
                    list.head = temp;
                    pre = temp;
                    flag = 0;
                    flag1 = 1;
                } else {
                    pre.next = temp;
                    pre = temp;
                    flag1 = 1;
                }

                for (int j = 0; j < m; j++) {
                    int a = sc.nextInt();
                    tempB = new Node(a);
                    if (flag1 == 1) {
                        temp.bottom = tempB;
                        preB = tempB;
                        flag1 = 0;
                    } else {
                        preB.bottom = tempB;
                        preB = tempB;
                    }
                }
            }
            // list.printList();
            GfG g = new GfG();
            Node root = g.flatten(list.head);
            list.printList(root);

            t--;
        }
    }
}
// } Driver Code Ends




/*Node class  used in the program
class Node
{
	int data;
	Node next;
	Node bottom;
	
	Node(int d)
	{
		data = d;
		next = null;
		bottom = null;
	}
}
*/
/*  Function which returns the  root of 
    the flattened linked list. */
class GfG
{
    Node merge(Node head1, Node head2) {
        Node newHead = new Node(-1), p1 = head1, p2 = head2;
        Node temp = newHead;
        while (p1 != null && p2 != null) {
            if (p1.data < p2.data) {
                Node nn = new Node(p1.data);
                temp.bottom = nn;
                p1 = p1.bottom;
                temp = temp.bottom;
            }
            else {
                Node nn = new Node(p2.data);
                temp.bottom = nn;
                p2 = p2.bottom;
                temp = temp.bottom;
            }
        }
        while (p1 != null) {
            Node nn = new Node(p1.data);
            temp.bottom = nn;
            p1 = p1.bottom;
            temp = temp.bottom;
        }
        while (p2 != null) {
            Node nn = new Node(p2.data);
            temp.bottom = nn;
            p2 = p2.bottom;
            temp = temp.bottom;
        }
        // temp = newHead.bottom;
        // while (temp!= null) {
        //     System.out.println(temp.data);
        //     temp = temp.bottom;
        // }
        return newHead.bottom;
    }
    
    Node flatten(Node head)
    {
	// Your code here
	    if (head == null)
	        return head;
    	Node curr = head, nextNode = head.next;
    	while (nextNode != null) {
    	    Node nnNode = nextNode.next;
    	   // System.out.println(curr.bottom.data);
    	   // System.out.println(curr.next.data);
    	    curr = merge(curr, nextNode);
    	    curr.next = nnNode;
    	    nextNode = curr.next;
    	}
    	return curr;
    }
}