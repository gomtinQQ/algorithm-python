'''
1096 : [기초-2차원배열] 바둑판에 흰 돌 놓기(설명)
바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
참고
가로번호, 세로번호를 사용할 수 있는 2차원 배열을 사용하면
이러한 형태를 쉽게 기록하고 사용할 수 있다. 물론 더 확장한 n차원 배열도 만들 수 있다.

INPUT:
바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력된다.
둘째 줄 부터 n+1 번째 줄까지 힌 돌을 놓을 좌표(x, y)가 n줄 입력된다.
n은 10이하의 자연수이고 x, y 좌표는 1 ~ 19 까지이며, 같은 좌표는 입력되지 않는다.

OUTPUT:
흰 돌이 올려진 바둑판의 상황을 출력한다.
흰 돌이 있는 위치는 1, 없는 곳은 0으로 출력한다.
'''
n = int(input())
location = []

#STEP1: 19*19 배열을 만들고 초기 값을 0으로준다.
checkerBoard = [[0 for col in range(19)] for row in range(19)]

#STEP2:좌표 입력(좌표를 입력하면 바둑판에서 해당 좌표 값을 1로 바꾼다.)
for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    checkerBoard[int(x-1)][int(y-1)]=1

#STEP4: 바둑판 출력
for i in checkerBoard:
    for j in i:
        print(j, end=" ")
    print()
