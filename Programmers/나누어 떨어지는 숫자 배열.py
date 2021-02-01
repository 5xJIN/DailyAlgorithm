"""
Min : 0.00ms, 10.1MB
Max : 2.76ms, 13.4MB
"""

def solution(arr, divisor):
    answer = []

    for dividend in arr:
        if not dividend % divisor:
            answer.append(dividend)

    if answer == []:
        return [-1]

    answer.sort()

    return answer