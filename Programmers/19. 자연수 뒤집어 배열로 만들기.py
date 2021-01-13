"""
Min : 0.00ms, 9.91MB
Max : 0.01ms, 10.2MB
"""

def solution(n):
    answer = []
    while n > 0:
        answer.append(n % 10)
        n = n // 10

    return answer