'''
문제: 하샤드 수
'''
def solution(x):
    sumNum = sum([int(i) for i in str(x)])
    if x % sumNum == 0:
        return True
    return False