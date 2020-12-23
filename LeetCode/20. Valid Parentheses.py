"""
# Runtime : 32 ms
# Memory : 14.4 MB
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "").replace("{}", "").replace("[]", "")

        return s == ""