class Solution:
    def minimumPushes(self, word: str) -> int:
        # store freq
        freq = [0]*26
        for x in word:
            freq[ord(x)-ord('a')] +=1
        freq.sort(reverse=True)
        ans=0
        for i in range(len(freq)):
            ans +=freq[i]*(i//8+1)       
        return ans