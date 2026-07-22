class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans=0
        for i in range(0,n):
            freq = [0]*26
            for j in range(i,n):
                mini = float('inf')
                maxi = float('-inf')

                idx = ord(s[j])-ord('a')
                # store freq
                freq[idx]+=1
                # substring freq's completed now
                # calculate min and max
                for t in range(0,26):
                    if(freq[t]!=0):
                        maxi = max(maxi,freq[t])
                        mini = min(mini,freq[t])
                # add in ans
                # print(maxi-mini)
                ans+=(maxi-mini)
            # inner for loops end
        #outer for loops end
        return ans
                    
