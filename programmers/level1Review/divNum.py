'''
문제: 나누어 떨어지는 숫자 배
'''
def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)