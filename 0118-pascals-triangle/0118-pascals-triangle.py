class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def calPascalForRow(n):
            lst=[]
            lastIdx=0
            if(n>0):
                lst.append(1)
            for i in range(1,n):
                colCal= int(((n-i)*lst[lastIdx])/i)
                lst.append(colCal)
                lastIdx+=1
            return lst
        # tryop = calPascalForRow(5)
        # print(tryop)
        ans=[]
        for i in range(1,numRows+1):
            # calculate pascal for each row
            ans.append(calPascalForRow(i))
        return ans

            