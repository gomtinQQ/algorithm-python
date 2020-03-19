'''
1368 : 평행사변형 출력하기 2
이번엔 공백의 방향까지 정하여 평행사변형을 만들자.
방향 정보는 다음과 같다.
L=왼쪽 아래에 공백
R=오른쪽 아래에 공백
다음 조건에 맞춰 평행사변형을 출력한다.
'''
h, k, d = input().split()
h, k= int(h), int(k)
# L일 때
if(d=="L"):
    for i in range(0, h):
        for j in range(0, i):
            print(' ', end='')
        for j in range(0, k):
            print('*', end='')
        print()
else:
    for i in range(h-1, -1, -1):
        for j in range(0, i):
            print(' ', end='')
        for j in range(0, k):
            print('*', end='')
        print()