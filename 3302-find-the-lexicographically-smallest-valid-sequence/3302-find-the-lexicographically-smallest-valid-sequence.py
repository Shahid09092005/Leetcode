class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # suf[j] = earliest index where word2[j:]
        # can be matched exactly
        suf = [n] * (m + 1)

        i = n - 1

        for j in range(m - 1, -1, -1):
            while i >= 0 and word1[i] != word2[j]:
                i -= 1

            if i < 0:
                break

            suf[j] = i
            i -= 1

        ans = []
        i = 0
        j = 0
        mismatch = 0

        while i < n and j < m:

            # Characters match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

                if j == m:
                    return ans

            # Use the one allowed mismatch
            elif mismatch == 0:

                # If this is the last character,
                # no suffix is left, so it is always valid.
                if j == m - 1:
                    ans.append(i)
                    j += 1
                    mismatch = 1
                    return ans

                # Otherwise, remaining characters must
                # be matched exactly after i.
                elif suf[j + 1] < n and suf[j + 1] > i:
                    ans.append(i)
                    j += 1
                    mismatch = 1

                    if j == m:
                        return ans

            i += 1

        return []