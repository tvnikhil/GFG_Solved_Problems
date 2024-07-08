#User function Template for python3

class Solution:
    def helper(self, maze, n, x, y, curPath, ans):
        if x == n - 1 and y == n - 1 and maze[x][y] == 1:
            ans.append(str(curPath))
            return
        if (x < 0 or x >= n) or (y < 0 or y >= n):
            return
        if maze[x][y] == 1:
            maze[x][y] = -1
            self.helper(maze, n, x+1, y, curPath+"D", ans)
            self.helper(maze, n, x-1, y, curPath+"U", ans)
            self.helper(maze, n, x, y+1, curPath+"R", ans)
            self.helper(maze, n, x, y-1, curPath+"L", ans)
            maze[x][y] = 1
        else:
            return
    
    def findPath(self, m, n):
        # code here
        if m[0][0] == 0:
            return []
        ans = []
        self.helper(m, n, 0, 0, "", ans)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends