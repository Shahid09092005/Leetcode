class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openC=0
        closeC=0
        for chr in s:
            if(chr=='('):
                openC+=1
            else:
                # see close so remove open by 1 otherwise add it
                closeC+=1
                if(openC>=1):
                    openC-=1
                    closeC-=1
        return abs(closeC+openC)