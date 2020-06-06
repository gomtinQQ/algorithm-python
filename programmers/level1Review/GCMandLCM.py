'''
문제: 최대공약수와 최소공배수
'''
def solution(n, m):
    num1, num2 = min(n, m), max(n, m)
    r = num2 % num1
    while r != 0:
        num1, r = r, (num1 % r)

    return [num1, int((n * m) / num1)]