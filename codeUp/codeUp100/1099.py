'''
1099 : [기초-2차원배열] 성실한 개미
미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
오른쪽 또는 아래쪽으로만 움직였다.

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.
단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며,
개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.
10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.
성실한 개미가 이동한 경로를 9로 표시해 출력한다.

'''
MAX_VALUE = 10
#STEP1-1. 미로를 만든다.
maze = [[0 for i in range(MAX_VALUE)] for j in range(MAX_VALUE)]

#STEP1-2. 미로의 값을 받는다.
for i in range(MAX_VALUE):
    temp = list(map(int, input().split()))
    for j in range(MAX_VALUE):
        maze[i][j] = temp[j]

#STEP2. 미로를 프린트하는 함수
def mazePrint():
    for i in range(MAX_VALUE):
        for j in  range(MAX_VALUE):
            print(maze[i][j],end=' ')
        print( )

#STEP3. ANT의 위치
x=1;y=1;

while(True):
    #STEP4-1. 오른쪽으로 이동 시도
    if(maze[x][y+1]==0 or maze[x][y+1]==2):
        #STEP5-1. 원래 좌표에 과자가 있을 경우
        if(maze[x][y]==2):
            maze[x][y]=9
            break
        else:
            maze[x][y]=9
        #STEP5-2. 오른쪽으로 이동
        y+=1
        #STEP5-3. 과자 확인
        if(maze[x][y]==2):
            maze[x][y]=9
            break
        #STEP5-4. 과자가 없음
        else:
            maze[x][y]=9
    #STEP6-1. 아래로 이동
    elif(maze[x+1][y]==0 or maze[x+1][y]==2):
        #6-2. 현재 위치 과자 확인
        if(maze[x][y]==2):
            maze[x][y]=9
            break
        else:
            maze[x][y]=9
        x+=1
        #STEP6-3. 과자 확인
        if(maze[x][y]==2):
            maze[x][y]=9
            break
        #STEP6-4. 과자 없으면 계속 이동
        else:
            maze[x][y]=9
    #STEP7. 이동 불가
    else:
        break

#STEP8. 미로 프린트
mazePrint()