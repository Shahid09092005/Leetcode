class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        fmax = smax = tmax = float('-inf')
        fmin = smin = tmin = float('inf')

        for x in nums:
            # Maintain three largest values
            if x >= fmax:
                tmax = smax
                smax = fmax
                fmax = x
            elif x >= smax:
                tmax = smax
                smax = x
            elif x > tmax:
                tmax = x

            # Maintain three smallest values
            if x <= fmin:
                tmin = smin
                smin = fmin
                fmin = x
            elif x <= smin:
                tmin = smin
                smin = x
            elif x < tmin:
                tmin = x

        return max(
            fmax * smax * tmax,
            fmin * smin * fmax
        )