"""
Min : 0.00ms, 10.2MB
Max : 0.96ms, 16.8MB
"""

def solution(arr):
    if len(arr)==1:
        return [-1]
    arr.remove(min(arr))
    return arr