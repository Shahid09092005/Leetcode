class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        openParethesis=0
        for ch in s:
            if ch=='(':
                openParethesis+=1
            elif(ch==')'):
                ans = max(ans,openParethesis)
                openParethesis-=1
            else:
                continue
        return ans

        