'''
문제: 정수 내림차순으로 배치하기
'''
def solution(n):
    answer = sorted(list(str(n)), reverse = True)
    return int(''.join(answer))