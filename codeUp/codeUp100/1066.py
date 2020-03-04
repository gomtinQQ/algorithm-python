'''
1066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)
세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
'''
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

if(x%2==0):
    print("even")
else:
    print("odd")

if(y%2==0):
    print("even")
else:
    print("odd")

if(z%2==0):
    print("even")
else:
    print("odd")