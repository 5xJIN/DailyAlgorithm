'''
Min : 0.00ms, 10.2MB
Max : 0.01ms, 10.3MB
'''

def solution(a, b):
    answer = ''
    resultList = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    lastdate = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    date = b - 1
    for i in range(a - 1):
        date += lastdate[i]

    answer = resultList[date % 7]
    return answer