class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        ans = []
        # character with their freq in freq
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        for _ in range(len(freq)):
            maxFreq = 0
            ke=''
            for ch in freq:
                if(freq.get(ch)>maxFreq):
                    maxFreq=freq.get(ch)
                    ke = ch
            # now add in the ans's list
            ans.append(ke*maxFreq)
            # mark ke is used
            freq[ke]=0
        # return ans
        return ''.join(ans) 

        
        