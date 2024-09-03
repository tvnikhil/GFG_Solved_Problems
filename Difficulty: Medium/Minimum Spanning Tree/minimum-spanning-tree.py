#User function Template for python3
import heapq as pq
from typing import List

class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizeOfSet = [1] * n
        
    def findParent(self, u):
        if u == self.parents[u]:
            return u
        self.parents[u] = self.findParent(self.parents[u])
        return self.parents[u]
    
    def unionBySize(self, u, v):
        upu, upv = self.findParent(u), self.findParent(v)
        if upu == upv:
            return
        upuSize, upvSize = self.sizeOfSet[upu], self.sizeOfSet[upv]
        if upuSize < upvSize:
            self.parents[upu] = upv
            self.sizeOfSet[upv] += self.sizeOfSet[upu]
        else:
            self.parents[upv] = upu
            self.sizeOfSet[upu] += self.sizeOfSet[upv]

# Kruskal's algorithm

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        que = []
        djs = DisjointSet(V)
        ans = 0
        
        for u in range(V):
            for v, wt in adj[u]:
                pq.heappush(que, (wt, u, v))
        
        while que:
            wt,u,v = pq.heappop(que)
            # wt,u,v = edge.wt, edge.u, edge.v
            uComp, vComp = djs.findParent(u), djs.findParent(v)
            if uComp == vComp:
                continue
            ans += wt
            djs.unionBySize(u, v)
        
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from typing import List

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        ob = Solution()

        print(ob.spanningTree(V, adj))

# } Driver Code Ends