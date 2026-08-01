class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(i,j):
            if(i>j):
                return 0
            if(i==j):
                return nums[i]
            choose_i = nums[i]+min(solve(i+2,j),solve(i+1,j-1))
            choose_j = nums[j]+min(solve(i+1,j-1),solve(i,j-2))
            return max(choose_i,choose_j)

        pl1=solve(0,len(nums)-1)
        totalScore = sum(nums)
        pl2 = totalScore-pl1
        if(pl1>=pl2):
            return True
        return False

        