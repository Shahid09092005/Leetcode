from typing import List
from collections import defaultdict
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:

        nums.sort()

        # Equivalent to map<int, int> factors
        factors = defaultdict(int)

        # Count how many numbers are divisible by each factor
        for num in nums:
            j = 1
            while j * j <= num:
                if num % j == 0:
                    factors[j] += 1
                    if j != num // j:
                        factors[num // j] += 1
                j += 1

        # Equivalent to map<int, long int> gcdCnt
        gcdCnt = defaultdict(int)

        # Traverse factors in descending order
        for factor in sorted(factors.keys(), reverse=True):

            val = factors[factor]
            pairs = val * (val - 1) // 2

            multiple = factor * 2
            while multiple <= nums[-1]:
                pairs -= gcdCnt[multiple]
                multiple += factor

            gcdCnt[factor] = pairs

        # Build prefix array
        prefix = []
        gcdValues = []

        total = 0

        for gcd in sorted(gcdCnt.keys()):
            if gcdCnt[gcd] == 0:
                continue

            total += gcdCnt[gcd]
            prefix.append(total - 1)
            gcdValues.append(gcd)

        # Answer queries
        answer = []

        for q in queries:
            idx = bisect_left(prefix, q)
            answer.append(gcdValues[idx])

        return answer