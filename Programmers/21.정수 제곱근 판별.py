"""
Min : 0.01ms, 10.2MB
Max : 0.02ms, 10.3MB
"""

def solution(n):
    sqrt = n ** (1 / 2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2

    return -1