# User function Template for python3

from collections import defaultdict
class Solution:
    def graphColoring(self, V, edges, m):
        graph = defaultdict(list)
        colors = [-1] * V
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def isSafe(node, color):
            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    return False
            return True
        
        def dfs(node):
            for color in range(m):
                if isSafe(node, color):
                    colors[node] = color
                    for child in graph[node]:
                        if colors[child] == -1:
                            if dfs(child) == False:
                                colors[node] = -1
                                return False
                    return True
            
            return False
        
        for i in range(V):
            if colors[i] == -1:
                if dfs(i) == False:
                    return False
        
        return True


#{ 
 # Driver Code Starts
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges_input = list(map(int, input().split()))
        m = int(input())
        edges = []

        # Populate the edges list with edge pairs
        for i in range(0, len(edges_input), 2):
            edges.append((edges_input[i], edges_input[i + 1]))

        solution = Solution()
        print("true" if solution.graphColoring(n, edges, m) else
              "false")  # Call the graph coloring function


if __name__ == "__main__":
    main()

# } Driver Code Ends