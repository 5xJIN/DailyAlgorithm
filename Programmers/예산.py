"""
Min : 0.00ms, 10.3MB
Max : 0.03ms, 10.3MB
"""
def solution(d: list, budget: int):
    d.sort()
    result = []
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0:
            break
        result.append(d[i])

    return len(result)