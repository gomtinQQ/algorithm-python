'''
문제: 정수 제곱근 판별
'''
def solution(n):
    s = n ** (1/2)
    if s % 1 == 0:
        return (s + 1) ** 2
    return -1