'''
문제: 두 정수 사이의 합
'''
def solution(a, b):
    minNum = min(a, b)
    maxNum = max(a, b)
    return sum(range(minNum, maxNum+1))

print(solution(5,3))