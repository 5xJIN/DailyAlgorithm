"""
Min : 0.00ms, 10MB
Max : 0.14ms, 10.2MB
"""

def solution(x, n):
    answer = []
    for i in range(1, n + 1):
        answer.append(x * i)

    return answer