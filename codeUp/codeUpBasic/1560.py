'''
1560 : [기초-함수작성] 함수로 두 정수의 차이 값 리턴하기
long long int 형 정수 두 개를 입력 받아
두 수의 차이값을 출력하시오.
단, 함수형 문제이므로 함수 f()만 작성하여 제출하시오.
'''
def f(x,y):
    if(x > y):
        return x-y
    else:
        return y-x

x, y = input().split()
x = int(x)
y = int(y)

print(f(x,y))