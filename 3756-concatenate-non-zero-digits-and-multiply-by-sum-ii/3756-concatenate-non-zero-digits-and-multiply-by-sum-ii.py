class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        prefix_num = [0] * (n + 1)
        prefix_sum = [0] * (n + 1)
        prefix_count = [0] * (n + 1)

        for i, ch in enumerate(s):
            digit = int(ch)

            prefix_num[i + 1] = prefix_num[i]
            prefix_sum[i + 1] = prefix_sum[i]
            prefix_count[i + 1] = prefix_count[i]

            if digit != 0:
                prefix_num[i + 1] = (prefix_num[i] * 10 + digit) % MOD
                prefix_sum[i + 1] += digit
                prefix_count[i + 1] += 1

        # powers of 10 for removing prefix digits
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        ans = []

        for l, r in queries:
            cnt_before = prefix_count[l]
            cnt_range = prefix_count[r + 1] - cnt_before

            # concatenate digits in range
            x = prefix_num[r + 1] - (
                prefix_num[l] * pow10[cnt_range] % MOD
            )
            x %= MOD

            digit_sum = prefix_sum[r + 1] - prefix_sum[l]

            ans.append((x * digit_sum) % MOD)

        return ans