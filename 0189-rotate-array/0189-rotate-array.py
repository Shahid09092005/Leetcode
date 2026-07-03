class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(nums:List[int],s:int,e:int):
            while(s<e):
                t = nums[s]
                nums[s] = nums[e]
                nums[e]=t
                s+=1
                e-=1
        le = len(nums)
        k=k%le
        rev(nums,0,le-1)
        # [7,6,5,4,3,2,1]
        rev(nums,0,k-1)
        rev(nums,k,le-1)
        return 
