
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # count each character freq
        freq = {}
        for x in s:
            freq[x] = freq.get(x,0)+1

        # Half counts and middle character(only one in s)
        halffreq = {}
        middle = ""

        for ch in sorted(freq):
            halffreq[ch] = (int)(freq[ch]//2)
            if freq[ch] % 2:
                middle = ch

        # pre-compute factorials till all the no. of char
        total_half = sum(halffreq.values())
        fact = [1] * (total_half + 1)
        for i in range(1, total_half + 1):
            fact[i] = fact[i - 1] * i

        # Count distinct permutations of remaining
        def count_perm(halffreq):
            rem = sum(halffreq.values())
            ways = 1

            for v in halffreq.values():
                if v:
                    ways *= comb(rem, v)
                    rem -= v

                    # no need to know numbers larger than k
                    if ways >= k:
                        return k

            return ways

        # Not enough palindromes
        if count_perm(halffreq) < k:
            return ""

        left_half = []


        while sum(halffreq.values()) > 0:

            for ch in sorted(halffreq): # goes a to z

                if halffreq[ch] == 0:
                    continue

                halffreq[ch] -= 1

                ways = count_perm(halffreq)

                if ways >= k:
                    left_half.append(ch)
                    break
                else:
                    k -= ways
                    halffreq[ch] += 1       

        leftpart = "".join(left_half)
        return leftpart + middle + leftpart[::-1]