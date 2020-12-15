"""
# Runtime : 64 ms
# Memory : 14.4 MB
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        maxSize = pow(2, 31)

        if 0 < x < maxSize - 1:
            origin = x
            revert = 0
            while (origin > 0):
                revert = revert * 10
                remainder = origin % 10
                origin = origin // 10
                revert += remainder

            if x == revert:
                return True

        else:
            if x == 0:
                return True

            elif x < 0 or (x % 10) == 0:
                return False
