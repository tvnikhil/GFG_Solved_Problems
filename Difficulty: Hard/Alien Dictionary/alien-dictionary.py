#User function Template for python3

class Solution:
    def findFirstDiff(self, str1, str2):
        ptr1, ptr2 = 0, 0
        while ptr1 < len(str1) and ptr2 < len(str2):
            if str1[ptr1] != str2[ptr2]:
                return (str1[ptr1], str2[ptr2])
            ptr1 += 1
            ptr2 += 1
        return ("", "")
    
    def dfs(self, src, adj, vis, stk):
        vis[src] = True
        for neigh in adj[src]:
            if vis[neigh] == False:
                self.dfs(neigh, adj, vis, stk)
        stk.append(src)
    
    def findOrder(self,alien_dict, N, K):
        adj = []
        for i in range(K):
            adj.append([])
        i = 1
        while i < N:
            diff = self.findFirstDiff(alien_dict[i-1], alien_dict[i])
            if diff[0] == "" or diff[1] == "":
                i += 1
                continue
            adj[ord(diff[0])-97].append(ord(diff[1])-97)
            i += 1
        vis = []
        for i in range(K):
            vis.append(False)
        topo = []
        stk = []
        for i in range(K):
            if vis[i] == False:
                self.dfs(i, adj, vis, stk)
        while len(stk) > 0:
            topo.append(chr(stk.pop() + 97))
        return topo


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends