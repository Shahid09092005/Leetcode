class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        # handling 0 idx of s
        if (s[0]=='I'):
            ans+=1
        elif(s[0]=='V'):
            ans+=5
        elif(s[0]=='D'):
            ans+=500
        elif(s[0]=='M'):
            ans+=1000
        elif(s[0]=='L'):
            ans+=50
        elif(s[0]=='C'):
            ans+=100
        else: # for X
            ans+=10
    
        for i in range(1,len(s)):
            if (s[i]=='I'):
                ans+=1
            elif(s[i]=='V'):
                if(s[i-1]=='I'):
                    ans-=1
                    ans+=4
                else:    
                    ans+=5
            elif(s[i]=='X'):
                if(s[i-1]=='I'):
                    ans-=1
                    ans+=9
                else:
                    ans+=10
            elif(s[i]=='L'):
                if(s[i-1]=='X'):
                    ans-=10
                    ans+=40
                else:
                    ans+=50
            elif(s[i]=='C'):
                if(s[i-1]=='X'):
                    ans-=10
                    ans+=90
                else:
                    ans+=100
            elif(s[i]=='D'):
                if(s[i-1]=='C'):
                    ans-=100
                    ans+=400
                else:
                    ans+=500
            else: #for M
                if(s[i-1]=='C'):
                    ans-=100
                    ans+=900
                else:
                    ans+=1000
        # ends for loop
        return ans
                    

        