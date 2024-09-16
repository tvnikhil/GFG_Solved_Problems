#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def helper(self, idx, arr, k, dp):
        if idx == 0:
            return 0
        if idx in dp:
            return dp[idx]
        
        minCost = float("inf")
        for i in range(idx-k, idx):
            if i < 0: continue
            cost = self.helper(i, arr, k, dp) + abs(arr[idx]-arr[i])
            minCost = min(minCost, cost)
        
        dp[idx] = minCost
        return minCost
    
    def minimizeCost(self, arr, k):
        # code here
        dp = {}
        dp[0] = 0
        return self.helper(len(arr)-1, arr, k, dp)

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minimizeCost(arr,k)
        print(res)
        t -= 1


# } Driver Code Ends