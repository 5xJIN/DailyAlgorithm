"""
Min : 0.01ms, 10.1MB
Max : 0.04ms, 10.2MB
"""

import math
def solution(progresses, speeds):
    days, answer = [], []
    for prg, spd in list(zip(progresses, speeds)):
        days.append(math.ceil((100-prg)/spd))

    cnt = 0
    for i in range(len(days)):
        if days[cnt] < days[i]:
            answer.append(i-cnt)
            cnt = i
    answer.append(len(days)-cnt)

    return answer
