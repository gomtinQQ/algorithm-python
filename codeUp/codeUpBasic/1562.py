'''
1562 : [기초-함수작성] 함수로 두 정수의 작은 값 리턴하기
int 형 정수 두 개를 입력 받아
그 중 작은 값을 출력하시오.
단, 함수형 문제이므로 함수 min()만 작성하여 제출하시오.
'''
def min(x, y):
    if(x > y):
        return y
    else:
        return x

x, y = input().split()
x = int(x)
y = int(y)

print(min(x, y))