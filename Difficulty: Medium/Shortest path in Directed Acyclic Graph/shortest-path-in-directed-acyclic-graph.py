#User function Template for python3

from typing import List

class Solution:
    def dfs(self, src, adj, vis, stk):
        vis[src] = True
        
        for neigh, _ in adj[src]:
            if vis[neigh] == False:
                self.dfs(neigh, adj, vis, stk)
        
        stk.append(src)
    
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj = []
        vis = []
        dist = []
        for i in range(n):
            adj.append([])
            vis.append(False)
            dist.append(float("inf"))
        for edge in edges:
            adj[edge[0]].append([edge[1], edge[2]])
        stk = []
        for i in range(n):
            if vis[i] == False:
                self.dfs(i, adj, vis, stk)
        #print(stk)
        dist[0] = 0
        while len(stk) > 0:
            src = stk.pop()
            srcCost = dist[src]
            for neigh, edgeCost in adj[src]:
                newCost = edgeCost + srcCost
                dist[neigh] = min(dist[neigh], newCost)
        for i in range(n):
            if dist[i] == float("inf"):
                dist[i] = -1
        return dist
                
#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends