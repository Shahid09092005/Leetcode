class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open = 0 
        ans=""
        for ch in s:
            if(ch=='('):
                open+=1
                if(open>1):
                    # list have append fuct. and "".join(lst) 
                    ans+='('
            else:
                if(open>1):
                    ans+=')'
                open-=1
        return ans
            
        