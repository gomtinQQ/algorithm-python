'''
1461 : [기초-배열연습] 2차원 배열 순서대로 채우기 1-2
다음과 같은 n*n 배열 구조를 출력해보자.

입력이 3인 경우 다음과 같이 출력한다.
3 2 1
6 5 4
9 8 7

입력이 5인 경우는 다음과 같이 출력한다.
5 4 3 2 1
10 9 8 7 6
15 14 13 12 11
20 19 18 17 16
25 24 23 22 21

입력이 n인 경우의 2차원 배열을 출력해보자.
'''
n = int(input())
n_array = [x for x in range(1, n*n+1)]
result = [n_array[i:i+n] for i in range(0, len(n_array), n)]

for i in range(n):
    for j in range(n-1, -1, -1):
        print(result[i][j], end=" ")
    print()
