#User function Template for python3

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for idx1 in range(1, m + 1):
            for idx2 in range(1, n + 1):
                if text1[idx1 - 1] == text2[idx2 - 1]:
                    dp[idx1][idx2] = 1 + dp[idx1 - 1][idx2 - 1]
                else:
                    dp[idx1][idx2] = max(dp[idx1 - 1][idx2], dp[idx1][idx2 - 1])
        
        return dp
    
	def all_longest_common_subsequences(self, s, t):
		dp = self.longestCommonSubsequence(s, t)
		m, n = len(s), len(t)
		ansLen = dp[m][n]
		ans = set()
		memo = {}
		
		def findAllLCS(m, n, curr):
		    if len(curr) == ansLen:
		        ans.add(curr[::-1])
		        return
		    if m < 1 or n < 1:
		        return
		    key = (m, n, curr)
		    if key in memo:
		        return
		    memo[key] = True
		    
		    if s[m-1] == t[n-1]:
		        findAllLCS(m-1,n-1,curr+s[m-1])
	        elif dp[m-1][n] == dp[m][n-1]:
	            findAllLCS(m-1, n, curr)
	            findAllLCS(m, n-1, curr)
            else:
                if dp[m-1][n] > dp[m][n-1]:
                    findAllLCS(m-1, n, curr)
                else:
                    findAllLCS(m, n-1, curr)
		
		findAllLCS(m, n, "")
		ans = list(ans)
		ans = sorted(ans)
		return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.all_longest_common_subsequences(s, t)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends