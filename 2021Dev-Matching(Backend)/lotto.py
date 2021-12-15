'''
Min : 0.00ms, 10.2MB
Max : 0.01ms, 10.2MB
'''

def solution(lottos: list, win_nums: list):

    plus = 0
    for lotto in lottos:
        if lotto == 0:
            plus = plus + 1

        elif lotto in win_nums:
            win_nums.remove(lotto)

    if len(win_nums) == 6:
        min_rank = 6
    else:
        min_rank = len(win_nums)+1

    if plus == 6:
        return [1, 6]

    return [min_rank-plus, min_rank]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
