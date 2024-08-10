#User function Template for python3
from typing import List

class Solution:
    
    def dfs(self, src, adj, vis, path):
        vis[src] = True
        path[src] = True
        
        for neigh in adj[src]:
            if vis[neigh] == False:
                if self.dfs(neigh, adj, vis, path) == True:
                    return True
            elif path[neigh] == True:
                return True
        
        path[src] = False
        return False
     
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        vis, path = [], []
        for i in range(V):
            vis.append(False)
            path.append(False)
        for i in range(V):
            if vis[i] == False:
                if self.dfs(i, adj, vis, path) == True:
                    return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

# } Driver Code Ends