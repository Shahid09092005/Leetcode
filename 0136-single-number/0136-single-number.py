class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR -> same nu. then 0 or diff. no. then 1
        x=1
        ans=0
        for x in nums:
            ans = ans^x
        return ans