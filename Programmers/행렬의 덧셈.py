"""
Min : 0.02ms, 10MB
Max : 28.91ms, 20.8MB
"""

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] = arr1[i][j] + arr2[i][j]
    return arr1
