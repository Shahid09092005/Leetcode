class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:

        freq = [0] * 26

        for ch in s:
            freq[ord(ch)-97] += 1

        half = [x // 2 for x in freq]

        middle = ""

        for i in range(26):
            if freq[i] % 2:
                middle = chr(i + 97)


        n = sum(half)

        # log factorial
        import math

        logfact = [0] * (n + 1)

        for i in range(1, n + 1):
            logfact[i] = logfact[i-1] + math.log(i)


        def count_perm():

            total = sum(half)

            # log(n! / a!b!c!)
            logways = logfact[total]

            for x in half:
                logways -= logfact[x]

            # if answer is definitely larger than k
            if logways > math.log(k):
                return k

            # here result is small, calculate exactly
            ans = math.factorial(total)

            for x in half:
                ans //= math.factorial(x)

            return ans


        if count_perm() < k:
            return ""


        left = []

        remaining = n

        while remaining:

            for i in range(26):

                if half[i] == 0:
                    continue

                half[i] -= 1
                remaining -= 1


                ways = count_perm()


                if ways >= k:
                    left.append(chr(i + 97))
                    break

                else:
                    k -= ways
                    half[i] += 1
                    remaining += 1


        left = "".join(left)

        return left + middle + left[::-1]