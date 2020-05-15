'''
1260: DFS와 BFS
문제:
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력: 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력: 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''
# N: 정점의 개수, M: 간선의 개수, V: 탐색을 시작할 정점의 번호
N, M, V = input().split()
N = int(N)
M = int(M)
V = int(V)
matrix = [[0] * (N+1) for i in range(N+1)]

# Adjacency matrix
for i in range(1, M+1):
    tmp = list(map(int, input().split()))
    matrix[tmp[0]][tmp[1]] = 1
    matrix[tmp[1]][tmp[0]] = 1

# DFS(Depth First Search)
def dfs(start_node, row, visited):
    visited.append(start_node)
    for search_node in range(len(row[start_node])):
        if row[start_node][search_node] and search_node not in visited:
            visited = dfs(search_node, row, visited)
    return visited

# BFS(Breadth First Search)
def bfs(start):
    queue = [start]
    visited = [start]

    while queue:
        node = queue.pop(0)
        for search_node in range(len(matrix[node])):
            if matrix[node][search_node] and search_node not in visited:
                visited.append(search_node)
                queue.append(search_node)

    return visited

print(*dfs(V, matrix, []))
print(*bfs(V))


