'''
1051 : [기초-비교연산] 두 정수 입력받아 비교하기3(설명)
두 정수(a, b)를 입력받아
b가 a보다 크거나 같으면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자.
'''

x,y = input().split()
x = int(x)
y = int(y)

if(y>x or x==y):
    print(1)
else:
    print(0)