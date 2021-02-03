"""
Min : 0.01ms, 10.2MB
Max : 57.01ms, 27.4MB
"""

def solution(numbers):
    numlist = list(map(str, numbers))
    numlist.sort(key=lambda x: x * 3, reverse=True)
    if numlist[0] == '0':
        return '0'

    return ''.join(numlist)