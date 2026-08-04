class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        arr = [0]*101
        maxi = float('-inf')
        mini = float('inf')
        for x in nums:
            arr[x]+=1
            maxi = max(maxi,x)
            mini = min(mini,x)
        lst=[]
        for x in range(mini,maxi+1):
            if arr[x]==0:
                lst.append(x)
        return lst


        