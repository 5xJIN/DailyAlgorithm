"""
Min : 0.01ms, 10.1MB
Max : 0.03ms, 10.3MB
"""

def solution(n):
    result = []

    for i in range(1, int((n ** 0.5)) + 1):
        if (n % i) == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)

    # result = set(result)
    return sum(result)