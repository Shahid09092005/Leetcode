class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        lst = list(arr)
        if len(arr)==0:
            return arr
        lst.sort()
        dct = {}
        smallestVal = lst[0]
        dct[smallestVal]=1
        rnk=1
        for i in range(1,len(lst)):
            if(lst[i-1]==lst[i]):
                dct[lst[i]]=rnk
            else:
                rnk+=1
                dct[lst[i]]=rnk
        # print(dct)  {10: 1, 20: 2, 30: 3, 40: 4}
        # as per arr value we must return their index in arr so
        lst=[]
        for i in range(0,len(arr)):
            rnk = dct.get(arr[i])
            # arr[i]=rnk
            lst.append(rnk)
        return lst
            
        
        