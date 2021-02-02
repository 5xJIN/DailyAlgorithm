"""
Min : 0.02ms, 10.2MB
Max : 0.03ms, 10.4MB
"""

def solution(x):
    arr = list(map(int, list(str(x))))
    divisor = sum(arr)
    if x % divisor == 0:
        return True

    return False