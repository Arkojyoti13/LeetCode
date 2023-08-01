class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(combination,start,k):
            if k == 0:
                result.append(combination[:])
                return
            # Recursively call dfs on unseen words
            for i in range(start,n+1):
                combination.append(i)
                dfs(combination,i+1,k-1)
                combination.pop()
        dfs([],1,k)
        return result