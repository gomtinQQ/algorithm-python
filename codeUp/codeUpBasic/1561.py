'''
1561 : [기초-함수작성] 함수로 두 정수의 큰 값 리턴하기
int 형 정수 두 개를 입력 받아
그 중 큰 값을 출력하시오.
단, 함수형 문제이므로 함수 max()만 작성하여 제출하시오.
전달된 두 정수 중 큰 값을 리턴하는 max() 함수의 예는 다음과 같다.
(다른 방법으로 작성해도 된다.)
'''
def max(x, y):
    if(x > y):
        return x
    else:
        return y

x, y = input().split()
x = int(x)
y = int(y)

print(max(x,y))
