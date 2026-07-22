class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        lst = [0]*26
        for x in s:
            idx = ord(x)-ord('a')
            lst[idx]+=1
        for x in t:
            idx = ord(x)-ord('a')
            lst[idx]-=1
        for x in lst:
            if(x!=0):
                return False
        return True