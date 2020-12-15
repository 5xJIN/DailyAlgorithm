"""
# Runtime : 60 ms
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

            return x == revert

        else:
            if x == 0:
                return True
            else:
                return False
