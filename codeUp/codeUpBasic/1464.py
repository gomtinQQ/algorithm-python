'''
1464 : [기초-배열연습] 2차원 배열 순서대로 채우기 1-5
다음과 같은 n*m 배열 구조를 출력해보자.

입력이 3 4인 경우 다음과 같이 출력한다.
12 11 10 9
8 7 6 5
4 3 2 1

입력이 4 5인 경우는 다음과 같이 출력한다.
20 19 18 17 16
15 14 13 12 11
10 9 8 7 6
5 4 3 2 1

입력이 n m인 경우의 2차원 배열을 출력해보자.
'''
n, m = input().split()
n = int(n) # row
m = int(m) # colum
n_array = [[x for x in range(n*m, 0, -1)][i:i+m] for i in range(0, n*m, m)]

for i in range(n):
    for j in range(m):
        print(n_array[i][j], end=" ")
    print()