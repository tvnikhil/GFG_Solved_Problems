//{ Driver Code Starts
import java.util.*;
class Sorting
{
	static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i]+" ");
        System.out.println();
    }
    
    // Driver program
    public static void main(String args[])
    {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while(T>0)
		{
			int n = sc.nextInt();
			int arr[] = new int[n];
			for(int i=0;i<n;i++)
				arr[i] = sc.nextInt();

			
			new Solution().quickSort(arr,0,n-1);
			printArray(arr);
		    T--;
		}
} }
// } Driver Code Ends


class Solution
{
    static void swap(int[] arr, int p, int q) {
        int temp = arr[p];
        arr[p] = arr[q];
        arr[q] = temp;
    }
    
    //Function to sort an array using quick sort algorithm.
    static void quickSort(int arr[], int low, int high)
    {
        // code here
        if (low >= high) return;
        int p = partition(arr, low, high);
        //System.out.println(p);
        quickSort(arr, low, p-1);
        quickSort(arr, p+1, high);
    }
    static int partition(int arr[], int low, int high)
    {
        // your code here
        int pivotIdx = low, left = low+1, right = high;
        while (left <= right) {
            while (left <= high && arr[left] <= arr[pivotIdx])
                left++;
            while (right >= low+1 && arr[right] > arr[pivotIdx])
                right--;
            if (left < right)
                swap(arr, left++, right--);
        }
        swap(arr, pivotIdx, right);
        return right;
    } 
}
