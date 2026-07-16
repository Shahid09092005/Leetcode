class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcdCal(a,b):
            while(a!=0):
                t=b%a
                b=a
                a=t
            return b
        prefixGcd = []
        maxi = 0
        for x in nums:
            tempMaxi = max(maxi,x)
            maxi = tempMaxi # assign max to maxi
            prefixGcd.append(gcdCal(tempMaxi,x))
        # now sort the prefixGcd
        prefixGcd.sort()
        # now taking smallest and largest pain and again calculate gcd
        st=0 # start
        en= len(prefixGcd)-1  # end
        ans=0  # initial sum
        while(st<en):
            ans += gcdCal(prefixGcd[st],prefixGcd[en])
            st+=1
            en-=1
            # n is odd, the middle element in the prefixGcd array remains unpaired and should be ignored.
        # return ans
        return ans
        