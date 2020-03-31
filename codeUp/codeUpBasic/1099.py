'''
1099 : [기초-2차원배열] 성실한 개미
개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
오른쪽 또는 아래쪽으로만 움직였다.

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며,
개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.
'''
MAX_VALUE = 10
maze = [[0 for i in range(MAX_VALUE)] for i in range(MAX_VALUE)]
for i in range(MAX_VALUE):
    temp = list(map(int, input().split()))
    for j in range(MAX_VALUE):
        maze[i][j] = temp[j]
x = 1 # 아래로 이동
y = 1 # 오른쪽 이동
stop = False

while(stop!=True):
    if(maze[x][y]==2):
        maze[x][y] = 9
        stop = True
    elif(maze[x][y+1]!=1):
        maze[x][y] = 9
        if(maze[x][y+1]==2):
            y = y+1
            maze[x][y] = 9
            stop = True
        else:
            y = y+1 # 계속 이동
            maze[x][y] = 9
    else: # 아래로 이동
        maze[x][y] = 9
        if(maze[x+1][y]==1):
            stop = True
        elif(maze[x+1][y]==2):
            x = x+1
            maze[x][y] = 9
            stop = True
        else:
            x = x+1
            maze[x][y] = 9

for i in range(MAX_VALUE):
    for j in range(MAX_VALUE):
        print(maze[i][j], end=" ")
    print()
