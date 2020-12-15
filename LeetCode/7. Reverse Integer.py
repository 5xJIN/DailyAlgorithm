"""
# Runtime : 24 ms
# Memory : 14.1 MB
"""
class Solution:
    def reverse(self, x: int) -> int:
        maxsize = pow(2, 31)

        unreverse = str(x)
        if x > 0:
            reverse = unreverse[::-1]
            result = int(reverse)
        elif x < 0:
            changeInt = unreverse[1:]
            reverse = changeInt[::-1]
            result = -int(reverse)
        else:
            return 0

        if -maxsize > result or result > maxsize - 1:
            return 0

        return result