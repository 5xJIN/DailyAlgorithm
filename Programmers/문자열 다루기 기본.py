"""
Min : 0.00ms, 10MB
Max : 0.01ms, 10.3MB
"""

def solution(s):
    if (len(s) != 4) and (len(s) != 6):
        return False
    elif s.isdigit() == True:
        return True

    return False