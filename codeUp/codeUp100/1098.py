'''
길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,
막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
(잉어, 붕어, 용 등 여러 가지가 적혀있다.)

격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,
격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고, 두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
'''
#STEP1-1: 격자판의 세로(h)와 가로(w)를 입력
h, w = input().split()
H = int(h)
W = int(w)
#STEP1-2: 놓을 수 있는 막대의 개수
n = int(input())

#STEP1-3: 각 막대의 길이(l), 방향(d), 좌표(x,y)를 저장
stickInfo = []
for i in range(n):
    l, d, x, y = input().split()
    stickInfo.append([int(l), int(d), int(x), int(y)])

#STEP2: 격자판을 생성한다.
checkerBoard = [[0 for i in range(W)] for j in range(H)]

#STEP3: 막대를 격자판에 놓는다.
for i in range(n):
    #STEP3-1: x, y에 막대의 길이, 방향 그리고 좌표를 저장한다.
    l = stickInfo[i][0]
    d = stickInfo[i][1]
    x = stickInfo[i][2]-1
    y = stickInfo[i][3]-1

    #STEP3-2: 막대 방향이 가로일 때
    if(d==0):
        for j in range(l):
        #STEP3-5: 막대의 길이 만큼 1로 변경
            checkerBoard[x][y+j]=1

    #STEP3-2: 막대 방향이 세로일 때
    elif(d==1):
        for j in range(l):
            checkerBoard[x+j][y]=1

#격자판을 출력한다.
for i in range(H):
    for j in range(W):
        print(checkerBoard[i][j], end=' ')
    print('')