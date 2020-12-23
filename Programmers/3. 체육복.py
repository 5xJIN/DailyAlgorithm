'''
Min : 0.01ms, 10.1MB
Max : 0.02ms, 10.2MB
'''

def solution(n, lost, reserve):
    answer = 0
    count = 0
    total = set(lost) & set(reserve)
    lost = list(filter(lambda x: x not in total, lost))
    reserve = list(filter(lambda x: x not in total, reserve))

    for l in lost:
        for i in [l - 1, l + 1]:
            if i in reserve:
                reserve.remove(i)
                count += 1
                break

    answer = n - (len(lost) - count)

    return answer