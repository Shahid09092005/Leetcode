class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcdCal(a, b):
            while a != 0:
                t = b % a
                b = a
                a = t
            return b
        sumOdd=n*n
        sumEven=n*(n+1)
        return gcdCal(sumOdd,sumEven)