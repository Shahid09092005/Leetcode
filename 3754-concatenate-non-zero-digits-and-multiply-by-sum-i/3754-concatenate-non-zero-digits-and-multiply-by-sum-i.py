class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=0
        nstr = str(n)
        x=0
        su=0
        for ch in nstr:
            if(ch!='0'):
                chInt = int(ch)
                x=x*10+chInt
                su+=chInt
        return x*su




