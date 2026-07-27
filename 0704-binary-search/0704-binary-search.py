class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def solu(nums,st,ed):
            while(st<=ed):
                mid = (int)(st-(st-ed)/2)
                if(nums[mid]==target):
                    return mid
                elif(nums[mid]<target):
                    st=mid+1
                else:
                    ed=mid-1
            return -1
        ans=solu(nums,0,len(nums)-1)
        return ans
        