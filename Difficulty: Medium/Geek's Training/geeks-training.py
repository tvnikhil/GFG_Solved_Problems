#User function Template for python3

class Solution:
    def maximumPoints(self, arr, n):
        # Code here
        dp = arr[n-1]
        for i in range(n-2,-1,-1):
            curr = [0] * 3
            for j in range(3):
                ans = float("-inf")
                for k in range(3):
                    if k != j:
                        ans = max(ans, dp[k])
                curr[j] = ans + arr[i][j]
            dp = list(curr)
        return max(dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        print(ob.maximumPoints(arr, n))
# } Driver Code Ends