"""
Min : 0.01ms, 10.1MB
Max : 2.24ms, 10.3MB
"""

def solution(s, n):
    s = list(s)
    up = ord('A')
    down = ord('a')

    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - up + n) % 26 + up)
        if s[i].islower():
            s[i] = chr((ord(s[i]) - down + n) % 26 + down)

    return ''.join(s)