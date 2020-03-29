'''
1096 : [기초-2차원배열] 바둑판에 흰 돌 놓기(설명)
바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
'''
chkbrd = [[0 for col in range(19)] for row in range(19)]
n = int(input())

for i in range(n):
    x,y = input().split()
    x = int(x)
    y = int(y)
    chkbrd[x-1][y-1] = 1

for i in range(len(chkbrd)):
    for j in range(len(chkbrd)):
        print(chkbrd[i][j], end=" ")
    print()