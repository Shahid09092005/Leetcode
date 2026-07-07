class Solution:
    def largestOddNumber(self, num: str) -> str:
        e = len(num)-1
        while(e>=0):
            if(int(num[e])%2!=0):
                return num[0:e+1]
            e -=1
        return ""