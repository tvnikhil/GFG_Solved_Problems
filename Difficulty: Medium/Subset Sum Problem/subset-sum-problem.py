#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, target):
        # code here 
        m, n = N, target+1
        dp = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = True
        if arr[0] <= target:
            dp[0][arr[0]] = True
        
        for i in range(1, m):
            for j in range(1, target+1):
                pick = False
                if j-arr[i] >= 0:
                    pick = dp[i-1][j-arr[i]]
                nonPick = dp[i-1][j]
                dp[i][j] = (pick or nonPick)
        
        return dp[m-1][target]
        

# class Solution:
#     def dfs(self, idx, target, arr, dp):
#         if target == 0:
#             return True
#         if idx == 0:
#             return (arr[0] == target)
#         if (idx, target) in dp:
#             return dp[(idx, target)]
        
#         pick = self.dfs(idx-1, target-arr[idx], arr, dp)
#         nonPick = self.dfs(idx-1, target, arr, dp)
#         dp[(idx, target)] = (pick or nonPick)
        
#         return dp[(idx, target)]
        
    
#     def isSubsetSum (self, N, arr, target):
#         # code here 
#         dp = {}
#         return self.dfs(N-1, target, arr, dp)

# class Solution:
#     def dfs(self, idx, curr, arr, target):
#         if idx <= len(arr)-1 and curr == target:
#             return True
#         if idx >= len(arr) or curr > target:
#             return False
        
#         pick = self.dfs(idx+1, curr+arr[idx], arr, target)
#         nonpick = self.dfs(idx+1, curr, arr, target)
        
#         return pick or nonpick
        
    
#     def isSubsetSum (self, N, arr, target):
#         # code here 
#         return self.dfs(0, 0, arr, target)
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends