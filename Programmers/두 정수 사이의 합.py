"""
Min : 0.00ms, 10.2MB
Max : 319.76ms, 10.2MB
"""

def solution(a, b):
    if a == b:
        return a

    if a > b:
        a, b = b, a

    answer = sum(range(a, b + 1))

    return answer


"""
# Min : 0.00ms, 10MB
# Max : 0.00ms, 10.3MB

def solution(a, b):
    return (abs(a-b)+1)*(a+b)//2

"""