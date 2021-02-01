'''
Min : 0.00ms, 10MB
Max : 0.01ms, 10.2MB
'''

def solution(array, commands):
    answer = []
    for command in commands:
        resultArray = array[command[0] - 1: command[1]]
        resultArray.sort()
        answer.append(resultArray[command[2] - 1])

    return answer