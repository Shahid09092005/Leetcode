class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # Hashing // Array or list O(26)
        freq=[0]*26
        for i in s:
            ordVal = ord(i)-ord('a') #ord()--> Unicode a-97 
            freq[ordVal]+=1
        # left right and mid
        n=len(s)
        left = ""
        mid=""
        for i in range(26): #i-> 0 to 25 asc
            if(freq[i]>=2):
                hffreq= (int)(freq[i]//2)
                left += chr(ord('a')+i)*hffreq
            if(freq[i]%2==1): # Med--> odd
                mid+=chr(ord('a')+i)
        ans = left+mid+left[::-1]
        return ans
        