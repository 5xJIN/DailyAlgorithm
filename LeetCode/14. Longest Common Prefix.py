"""
# Runtime : 28 ms
# Memory : 14.3 MB
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) == 0:
            return result

        strs.sort()
        for first, end in zip(strs[0], strs[-1]):
            if first == end:
                result += first
            else:
                break

        return result