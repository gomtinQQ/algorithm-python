'''
1057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기
두 개의 참(1) 또는 거짓(0)이 입력될 때,
참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.
'''
x,y = input().split()
x = int(x)
y = int(y)

if(x==y):
    print(1)
else:
    print(0)