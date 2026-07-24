class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX = 2048 #maximum number form by using1 <= nums[i] <= 1500 
        dp = [False] * MAX
        dp[0] = True # bcz XOR property :  0 ^ num = num

        for _ in range(3): # need to form a triplates
            new_dp = [False] * MAX

            for x in range(MAX):
                if dp[x]:
                    for num in nums:
                        new_dp[x ^ num] = True

            dp = new_dp

        return sum(dp)