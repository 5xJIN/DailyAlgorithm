"""
Min : 0.01ms, 10MB
Max : 0.02ms, 10.2MB
"""

def solution(strings, n):
    answer = sorted(sorted(strings), key=lambda x: x[n])

    return answer