class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def solve(i,j,dp):
            if(i>j):
                return 0
            if(i==j):
                return piles[i]
            if(arr[i][j]!=-1):
                return dp[i][j]
            
            choose_i = piles[i]+min(solve(i+2,j,dp),solve(i+1,j-1,dp))
            choose_j = piles[j]+min(solve(i+1,j-1,dp),solve(i,j-2,dp))
            dp[i][j] = max(choose_i,choose_j)
            return dp[i][j]
        # momoization
        n = len(piles)
        arr = [[-1]*n for _ in range(n)]
        pl1=solve(0,n-1,arr)
        totalScore = sum(piles)
        pl2 = totalScore-pl1
        if(pl1>=pl2):
            return True
        return False
        