'''
Min : 0.00ms, 10MB
Max : 0.00ms, 10.2MB
'''


def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        index = len(s) // 2
        answer = s[index - 1:index + 1]
    else:
        answer = s[len(s) // 2]

    return answer