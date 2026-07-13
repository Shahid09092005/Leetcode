class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        ans = []
        s = "123456789"

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                num = int(s[i:j])

                if low <= num <= high:
                    ans.append(num)

        return sorted(ans)