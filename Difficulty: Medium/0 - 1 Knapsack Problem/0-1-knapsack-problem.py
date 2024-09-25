#User function Template for python3

class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
        # code here
        n = W+1
        dp = [0] * n
        for i in range(n):
            dp[i] = val[0] if i >= wt[0] else 0
        
        for i in range(1, len(wt)):
            for j in range(n-1, 0, -1):
                nonpick = dp[j]
                pick = float("-inf")
                if j-wt[i] >= 0:
                    pick = val[i] + dp[j-wt[i]]
                dp[j] = max(pick, nonpick)
        
        return dp[W]

# class Solution:
#     #Function to return max value that can be put in knapsack of capacity W.
#     def knapSack(self,W, wt, val):
#         # code here
#         m, n = len(wt), W+1
#         dp = [[0 for _ in range(n)] for _ in range(m)]
#         for i in range(n):
#             if i >= wt[0]:
#                 dp[0][i] = val[0]
        
#         for i in range(1, m):
#             for j in range(1, n):
#                 nonpick = dp[i-1][j]
#                 pick = float("-inf")
#                 if j-wt[i] >= 0:
#                     pick = val[i] + dp[i-1][j-wt[i]]
#                 dp[i][j] = max(pick, nonpick)
        
#         return dp[m-1][W]

# class Solution:
    
#     def dfs(self, idx, W, wt, val, dp): # gives max value that we can get
#         if idx == 0:
#             if W >= wt[0]:
#                 return val[0]
#             return 0
#         if (idx, W) in dp:
#             return dp[(idx, W)]
        
#         pick = float("-inf")
#         if W-wt[idx] >= 0:
#             pick = val[idx] + self.dfs(idx-1, W-wt[idx], wt, val, dp)
#         nonpick = self.dfs(idx-1, W, wt, val, dp)
#         dp[(idx, W)] = max(pick, nonpick)
        
#         return dp[(idx, W)]
                
    
#     #Function to return max value that can be put in knapsack of capacity W.
#     def knapSack(self,W, wt, val):
#         # code here
#         dp = {}
#         return self.dfs(len(wt)-1, W, wt, val, dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val))

# } Driver Code Ends