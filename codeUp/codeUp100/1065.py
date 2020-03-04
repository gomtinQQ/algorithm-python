'''
1065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)
세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.
'''
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

if (x%2==0):
    print(x)

if (y%2==0):
    print(y)

if (z%2==0):
    print(z)