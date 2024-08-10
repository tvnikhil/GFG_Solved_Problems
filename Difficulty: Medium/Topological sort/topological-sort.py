class Solution:
    
    def dfs(self, src, adj, vis, stk):
        vis[src] = True
        for neigh in adj[src]:
            if vis[neigh] == False:
                self.dfs(neigh, adj, vis, stk)
        stk.append(src)
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        vis = []
        for i in range(V): vis.append(False)
        stk = []
        for i in range(V):
            if vis[i] == False:
                self.dfs(i, adj, vis, stk)
        path = []
        while len(stk) > 0:
            path.append(stk.pop())
        return path



#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends