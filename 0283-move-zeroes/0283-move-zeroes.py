class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt=0
        for x in nums:
            if(x==0):
                cnt+=1
        x=0
        for i in range(0,len(nums)):
            if(nums[i]!=0):
                nums[x]=nums[i]
                x+=1
        for _ in range(0,cnt):
            nums[x]=0
            x+=1
        return
