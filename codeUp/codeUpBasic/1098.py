'''
1098 : [기초-2차원배열] 설탕과자 뽑기
막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
(잉어, 붕어, 용 등 여러 가지가 적혀있다.)
격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,
격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
'''
h, w = input().split()
n = int(input())
h = int(h)
w = int(w)
x_lst = []
y_lst = []
l_lst = []
d_lst = []
chkbrd = [[0 for column in range(w)] for row in range(h)]

for i in range(n):
    l, d, x, y = input().split()
    x_lst.append(int(x)-1)
    y_lst.append(int(y)-1)
    l_lst.append(int(l)) # 막대 길이
    d_lst.append(int(d)) # 막대를 놓는 방향(0: 가로, 1: 세로)

for i in range(n):
    x = x_lst[i]
    y = y_lst[i]
    l = l_lst[i]
    d = d_lst[i]
    if (d == 0):
        for j in range(l):
            chkbrd[x][y] = 1
            y = y+1
    else:
        for j in range(l):
            chkbrd[x][y] = 1
            x = x+1

for i in range(h):
    for j in range(w):
        print(chkbrd[i][j], end=" ")
    print()
