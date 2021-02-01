"""
Min : 0.00ms, 10.1MB
Max : 0.07ms, 10.2MB
"""

def solution(s):
    answer = ""
    answer = answer.join(sorted(s, reverse=True))
    return answer