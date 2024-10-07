#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        m, n = N, W+1
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        
        prev = [0] * n
        for wtLeft in range(n):
            if wtLeft >= wt[0]:
                prev[wtLeft] = val[0]*(wtLeft // wt[0])
        curr = list(prev)
        
        for idx in range(1, m):
            for wtLeft in range(n):
                pick = -1
                if wtLeft >= wt[idx]:
                    pick = val[idx] + curr[wtLeft-wt[idx]]
                nonpick = prev[wtLeft]
                curr[wtLeft] = max(pick, nonpick)
            prev = curr
        
        return prev[n-1]
        
        # for idx in range(m):
        #     for wtLeft in range(n):
        #         if idx == 0:
        #             if wtLeft >= wt[idx]:
        #                 dp[idx][wtLeft] = val[idx] * (wtLeft // wt[idx])
        #         else:
        #             pick = -1
        #             if wtLeft >= wt[idx]:
        #                 pick = val[idx] + dp[idx][wtLeft-wt[idx]]
        #             nonpick = dp[idx-1][wtLeft]
        #             dp[idx][wtLeft] = max(pick, nonpick)
        
        # return dp[m-1][n-1]

# class Solution:
#     def knapSack(self, N, W, val, wt):
#         # code here
#         dp = {}
        
#         def dfs(idx, wtLeft):
#             if idx == 0:
#                 if wtLeft >= wt[idx]:
#                     return val[idx] * (wtLeft // wt[idx])
#                 return 0
#             if (idx, wtLeft) in dp:
#                 return dp[(idx, wtLeft)]
            
#             pick = -1
#             if wtLeft >= wt[idx]:
#                 pick = val[idx] + dfs(idx, wtLeft-wt[idx])
#             nonpick = dfs(idx-1, wtLeft)
#             dp[(idx, wtLeft)] = max(pick, nonpick)
            
#             return dp[(idx, wtLeft)]
        
#         return dfs(N-1, W)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends