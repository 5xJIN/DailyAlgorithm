"""
Min : 0.02ms, 10.2MB
Max : 0.03ms, 10.4MB
"""

def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    answer = ''.join(answer)
    return int(answer)