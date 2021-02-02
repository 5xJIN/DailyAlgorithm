"""
Min : 0.00ms, 10.1MB
Max : 0.00ms, 10.3MB
"""

def solution(phone_number):
    return '*'*len(phone_number[:-4]) + phone_number[-4:]