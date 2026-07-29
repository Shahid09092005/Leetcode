class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def isSorted(lst):
            for i in range(1,len(lst)):
                if(lst[i-1]<=lst[i]):
                    continue
                else:
                    return False
            return True
        
        def SmallestAdjacentIdx(lst):
            l=0
            smallAdjSum = float('inf')
            for i in range(1,len(lst)):
                if(smallAdjSum>(lst[i-1]+lst[i])):
                    smallAdjSum = lst[i-1] + lst[i]
                    l=i-1
            return l
        def adjSum(l,r,lst):
            return lst[:l] + [lst[l] + lst[r]] + lst[r+1:]
        # already sorted 
        if(isSorted(nums)):
            return 0
        ans=0    
        lst = nums
        while(not isSorted(lst)):
            leftidx = SmallestAdjacentIdx(lst)
            lst = adjSum(leftidx,leftidx+1,lst)
            ans+=1


        return ans
        
        