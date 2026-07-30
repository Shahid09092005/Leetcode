class Solution:
    def minimumPushes(self, word: str) -> int:
        totalEle=len(word)
        # left = totalEle%8
        # eachKey = totalEle-left
        st = {}
        ans=0
        for i in range(2,10):
            st[i] = ''
        idx=2
        for x in word:
            st[idx]+=x
            ans += len(st[idx])
            print(st[idx],x,ans,idx)
            idx+=1
            if(idx==10):
                idx=2
        return ans

