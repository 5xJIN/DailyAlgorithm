"""
Min : 0.00ms, 10.2MB
Max : 0.20ms, 10.2MB
"""
def solution(num):
    count = 1
    while count < 500:
        if num == 1:
            return count
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1

    return -1

'''
def solution(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        count += 1

        if count >= 500:
            return -1

    return count
'''
