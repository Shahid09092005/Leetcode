class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = set()
        freq = dict()
        for i in range(0,len(s)):
            if s[i] in freq :
                if(t[i]!=freq[s[i]]):
                    return False
                # if s[i] in st:
                #     return False
                st.add(t[i])
            else:
                freq[s[i]] = t[i]
                if(t[i] in st):
                    return False
                st.add(t[i])
        # ends for loop
        return True