class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        arr = [0]*101
        for x in nums:
            arr[x]+=1
        mini = min(nums)
        maxi = max(nums)
        lst=[]
        for x in range(mini,maxi+1):
            if arr[x]==0:
                lst.append(x)
        return lst


        