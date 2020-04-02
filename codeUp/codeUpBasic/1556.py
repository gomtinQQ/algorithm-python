'''
1556 : [기초-함수작성] 함수로 n! 리턴하기
int 형 정수 한 개를 입력 받아
n!(팩토리얼)을 계산해 출력하시오.
(0 <= n <= 20)
n!(팩토리얼)은 1부터 n까지 모두 곱한 수를 의미한다.
5! 은 1*2*3*4*5 = 120 이다.
단, 함수형 문제이므로 함수 f()만 작성하여 제출하시오.
'''
def f(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

n = int(input())
print(f(n))
