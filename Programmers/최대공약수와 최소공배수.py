"""
Min : 0.00ms, 10.1MB
Max : 0.00ms, 10.3MB
"""

def solution(n, m):
    a = n
    b = m
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b

    multiple = n * m // b

    return [b, multiple]