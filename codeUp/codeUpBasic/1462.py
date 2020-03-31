'''
1462 : [기초-배열연습] 2차원 배열 순서대로 채우기 1-3
다음과 같은 n*n 배열 구조를 출력해보자.

입력이 3인 경우 다음과 같이 출력한다.
1 4 7
2 5 8
3 6 9

입력이 5인 경우는 다음과 같이 출력한다.
1 6 11 16 21
2 7 12 17 22
3 8 13 18 23
4 9 14 19 24
5 10 15 20 25

입력이 n인 경우의 2차원 배열을 출력해보자.
'''
n = int(input())
lst = [x for x in range(1, n*n+1)]
n_array = [lst[i:i+n] for i in range(0, n*n, n)]

for i in range(n):
    for j in range(n):
        print(n_array[j][i], end=" ")
    print()
