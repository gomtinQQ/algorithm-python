'''
1566 : [기초-함수작성] 함수로 거듭제곱 리턴하기
int 형 자연수 두 개(a, n)를 입력 받아
거듭 제곱(exponentiation, a^n)한 결과 값을 출력하시오.
단, 함수형 문제이므로 함수 pow()만 작성하여 제출하시오.
'''
def pow(a, n):
    return (a**n)

a, n = input().split()
a = int(a)
n = int(n)
print(pow(a, n))