class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def cal(x,n):
            lmt =10**9 + 7
            if(n==1):
                return x
            if(n==0):
                return 1
            half = cal(x,n//2)
            if(n%2==0):
                return (half*half)%lmt
            return (half*half*x)%lmt
        lmt =10**9 + 7
        evenPlaces = (n+1)//2 
        evenChoices = 5
        oddPlaces=  n//2
        oddChoices=4
        EvenAns = cal(evenChoices,evenPlaces)
        oddAns = cal(oddChoices,oddPlaces)
        return ((EvenAns)*(oddAns))%lmt
        