#User function Template for python3

class Solution:
    # def compute(self, n, h, dp):
    #     if n == 0:
    #         return 0
    #     if n in dp:
    #         return dp[n]
    #     left = self.compute(n-1, h, dp) + abs(h[n]-h[n-1])
    #     if n > 1:
    #         right = self.compute(n-2, h, dp) + abs(h[n]-h[n-2])
    #     else:
    #         right = float("inf")
    #     dp[n] = min(left, right)
    #     return dp[n]
    
    def minimumEnergy(self, h, n):
        # Code here
        dp = [0 for _ in range(n)]
        
        for i in range(1, n):
            pos1 = dp[i-1]+abs(h[i]-h[i-1])
            pos2 = dp[i-2]+abs(h[i]-h[i-2]) if i > 1 else float("inf")
            dp[i] = min(pos1, pos2)
        
        return dp[n-1]
        # return self.compute(n-1, height, dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))
# } Driver Code Ends