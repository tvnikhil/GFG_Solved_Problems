#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
		m, n = len(arr), sum+1
		mod = (10**9)+7
		dp = [[0 for _ in range(n)] for _ in range(m)]
		for i in range(m):
		    dp[i][0] = 1
		if arr[0] <= n-1:
		    dp[0][arr[0]] = 1
        if arr[0] == 0:
            dp[0][0] = 2
		
		for idx in range(1, m):
		    for target in range(n):
		        nonpick = dp[idx-1][target]
		        pick = 0
		        if target-arr[idx] >= 0:
		            pick = dp[idx-1][target-arr[idx]]
                dp[idx][target] = (nonpick+pick) % mod
		
		return dp[m-1][n-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends