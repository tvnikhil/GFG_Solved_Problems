#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def tdc(self, n, memo):
        if n in memo:
            return memo[n]
        memo[n] = (self.tdc(n-1,memo)+self.tdc(n-2,memo)) % (10**9+7)
        return memo[n]
    
    def topDown(self, n):
        # Code here
        memo = {}
        memo[0], memo[1] = 0, 1
        ans = self.tdc(n, memo)
        # print("td", ans)
        return ans
        
    def bottomUp(self, n):
        # Code here
        dp = [0 for _ in range(n+1)]
        dp[0], dp[1] = 0, 1
        
        for i in range(2,n+1):
            dp[i] = (dp[i-1]+dp[i-2]) % (10**9+7)
        # print("bu", dp[n])
        
        return dp[n]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        topDownans=ob.topDown(n);
        bottomUpans=ob.bottomUp(n);
        if(topDownans!=bottomUpans):
            print(-1)
        else:
            print(bottomUpans)
# } Driver Code Ends