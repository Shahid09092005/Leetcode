class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        cntSurroundBy0Of1=[]
        cnt1=0
        lenS=len(s)
        cnt0=0
        for i in range(0,lenS):
            ch = s[i]
            if(ch=='0'):
                cnt0+=1
            else:
                cnt1+=1
                if(cnt0!=0):
                    cntSurroundBy0Of1.append(cnt0)
                cnt0=0
        if(s[lenS-1]=='0'):
             cntSurroundBy0Of1.append(cnt0)
        # now take maximum pair
        maxiPair = 0
        for i in range(1,len(cntSurroundBy0Of1)):
            maxiPair = max(maxiPair,cntSurroundBy0Of1[i-1]+cntSurroundBy0Of1[i])
        return maxiPair+cnt1

                