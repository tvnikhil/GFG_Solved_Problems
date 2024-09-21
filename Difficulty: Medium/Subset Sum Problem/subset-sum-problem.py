#User function Template for python3
class Solution:
    def dfs(self, idx, target, arr, dp):
        if target == 0:
            return True
        if idx < 0:
            return False
        if (idx, target) in dp:
            return dp[(idx, target)]
        
        pick = self.dfs(idx-1, target-arr[idx], arr, dp)
        nonPick = self.dfs(idx-1, target, arr, dp)
        dp[(idx, target)] = (pick or nonPick)
        
        return dp[(idx, target)]
        
    
    def isSubsetSum (self, N, arr, target):
        # code here 
        dp = {}
        return self.dfs(N-1, target, arr, dp)

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