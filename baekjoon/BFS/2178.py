'''
2178: 미로 탐색

문제:
N×M크기의 배열로 표현되는 미로가 있다.
1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력:
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
각각의 수들은 붙어서 입력으로 주어진다.

출력:
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
'''
N, M = input().split()
N = int(N)
M = int(M)
maze = []
for i in range(N):
    maze.append(list(map(int, input())))

def bfs(maze, N, M):
    q = []
    q.append((0, 0)) # x=0, y=0 : start Point
    visited = [[0 for i in range(M)]for i in range(N)]
    visited[0][0] = 1 # visited 처리
    dx = [0,0,1,-1] # x_move
    dy = [1,-1,0,0] # y_move
    escape = False

    while escape != True:
        x, y = q.pop(0)
        if x == N-1 and  y == M-1:
            escape = True
            break

        for i in range(4):
            if x + dx[i] >= 0 and y + dy[i] >= 0 and x + dx[i] < N and y + dy[i] < M:
                if maze[x + dx[i]][y + dy[i]] == 1 and visited[x + dx[i]][y + dy[i]] == 0:
                    visited[x + dx[i]][y + dy[i]] = visited[x][y] + 1
                    q.append((x + dx[i], y + dy[i]))
    return visited[N-1][M-1]

print(bfs(maze, N, M))