'''
Min : 0.01ms, 10.1MB
Max : 3.84ms, 10.3MB
'''

def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count1, count2, count3 = 0, 0, 0

    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            count1 += 1
        if answers[i] == second[i % len(second)]:
            count2 += 1
        if answers[i] == third[i % len(third)]:
            count3 += 1

    match = [count1, count2, count3]

    for person, score in enumerate(match):
        if score == max(match):
            answer.append(person + 1)

    return answer