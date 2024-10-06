
from typing import List


class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        # code here
        totSum = sum(arr)
        mod=int(1e9+7)
        
        if (totSum - d) < 0 or (totSum - d) % 2:
            return 0
            
        def findWays(num, tar):
            n = len(num)
        
            prev = [0] * (tar + 1)
            
            if num[0] == 0:
                prev[0] = 2  # 2 cases - pick and not pick
            else:
                prev[0] = 1  # 1 case - not pick
            
            if num[0] != 0 and num[0] <= tar:
                prev[num[0]] = 1  # 1 case - pick
            
            for ind in range(1, n):
                cur = [0] * (tar + 1)
                for target in range(tar + 1):
                    notTaken = prev[target]
            
                    taken = 0
                    if num[ind] <= target:
                        taken = prev[target - num[ind]]
                
                    cur[target] = (notTaken + taken) % mod
                prev = cur
            return prev[tar]
        
        return findWays(arr, (totSum - d) // 2)

#{ 
 # Driver Code Starts

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
        
        n = int(input())
        
        
        d = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.countPartitions(n, d, arr)
        
        print(res)
        

# } Driver Code Ends