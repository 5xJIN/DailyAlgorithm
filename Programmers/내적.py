"""
Min : 0.01ms, 10.2MB
Max : 0.17ms, 10.2MB
"""

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer

"""
def solution(a, b):
    answer = sum([x*y for x,y in zip(a,b)])

    return answer
"""