class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        i=0
        while(i<=n-3):
            if(i>0 and nums[i]==nums[i-1]):
                i+=1
                continue
            st=i+1
            ed=n-1
            while(st<ed):
                tSum=nums[i]+nums[st]+nums[ed]
                if(tSum==0):
                    ans.append([nums[i],nums[st],nums[ed]])
                    st+=1
                    ed-=1
                    while(st<ed and nums[st]==nums[st-1]):
                        st+=1
                    while(st<ed and nums[ed]==nums[ed+1]):
                        ed-=1
                elif(tSum>0):
                    # add smaller element
                    ed-=1
                elif(tSum<0):
                    # st+=1
                    st+=1
            i+=1
        return ans
        

        