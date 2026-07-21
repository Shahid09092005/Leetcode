class Solution:
    def smallestSubsequence(self, s: str) -> str:
        st=[]
        freq={}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        for ch in s:
            # decrease current element freq
            freq[ch]=freq.get(ch)-1
            if ch in st:
                continue
            while len(st)!=0 and st[-1]>ch and freq[st[-1]]>0:
                st.pop()
            st.append(ch)
        return ''.join(st)