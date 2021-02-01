"""
Min : 0.00ms, 10.1MB
Max : 0.00ms, 10.2MB
"""

def solution(n):
    answer = 0
    while n > 0:
        answer += n%10
        n = n//10

    return answer