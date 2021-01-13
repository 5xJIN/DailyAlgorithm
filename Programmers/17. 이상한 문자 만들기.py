"""
Min : 0.01ms, 10.2MB
Max : 0.04ms, 10.1MB
"""

def solution(s):
    s = list(s)
    c = 0
    for i in range(len(s)):
        if s[i] != ' ':
            if c % 2 == 0:
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
            c += 1
        else:
            c = 0

    return ''.join(s)
