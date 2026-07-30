class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort 2D array on basic of first starting value 
        intervals.sort(key=lambda x: x[0])
        ost = intervals[0][0]
        oed=intervals[0][1]
        ans=[]
        for i in range(1,len(intervals)):
            nst = intervals[i][0]
            ned=intervals[i][1]
            if(oed>=nst):
                ost=min(ost,nst)
                oed=max(ned,oed)
            else:
                # append
                temp = []
                temp.append(ost)
                temp.append(oed)
                ans.append(temp)
                ost=nst
                oed=ned
        # append last ost,oed
        temp = []
        temp.append(ost)
        temp.append(oed)
        ans.append(temp)
        return ans
