class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        ans=[]
        temp=[]
        i=len(s)-1
        while i>=0:
            while(i>=0 and s[i]!=' '):
                temp.append(s[i])
                i-=1
            # now we encounter with space
            while(i>=0 and s[i]==' '):
                i-=1
            if(len(ans)==0):
                ans.append(''.join(reversed(temp)))
            else:
                ans.append(' ')
                ans.append(''.join(reversed(temp)))
            temp=[]
        return ''.join(ans)
