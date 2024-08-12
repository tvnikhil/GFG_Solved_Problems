#User function Template for python3

class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adj = []
        dist = []
        vis = []
        for i in range(n):
            dist.append(-1)
            adj.append([])
            vis.append(False)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        #print(adj)
        que = [src]
        vis[src] = True
        level = 0
        while len(que) > 0:
            #print(que)
            size = len(que)
            for i in range(size):
                node = que.pop(0)
                dist[node] = level
                for neigh in adj[node]:
                    if vis[neigh] == False:
                        vis[neigh] = True
                        que.append(neigh)
            level += 1
        return dist
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends