'''
def solution(number, k):
    answer = ''
    number = list(number)

    if len(set(number)) == 1:
        return ''.join(number[:k])

    c = len(number) - k

    for i in range(1, c):
        index = c - i
        num = sorted(number[:-index], reverse=True)[0]
        number = number[number.index(num) + 1:]
        answer += num

    answer += number[-1]

    return answer
'''


def solution(number, k):
    number = list(number)
    first = sorted(number[:-(len(number) - k)], reverse=True)[0]
    answer = first
    k-=1
    number = number[number.index(first) + 1:]

    for i in number:
        while len(answer)>0 and answer[-1] < i and k>0:
            k-=1
            answer = answer[:-1]
        answer+=i
        if len(number[number.index(i)+1:])==k:
            answer += number[number.index(i)+1:]
    # if k>0:
    #     for i in number[:-k]:
    #         answer+=i
    return answer


# print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
print(solution("999",2))
print(solution("99991",3))
print(solution("111119",3))
print(solution("54329",4))