'''
1555 : [기초-함수작성] 함수로 n까지의 합 리턴하기
int 형 정수 한 개를 입력 받아
1부터 n까지의 정수합을 계산해 출력하시오.
(0 <= n <= 10000000)
단, 함수형 문제이므로 함수 f()만 작성하여 제출하시오.
'''
def f(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

n = int(input())
print(f(n))