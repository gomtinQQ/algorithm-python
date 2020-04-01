'''
1469 : [기초-배열연습] 2차원 배열 지그재그 채우기 2-2
다음과 같은 n*n 배열 구조를 출력해보자.

입력이 3인 경우 다음과 같이 출력한다.
3 2 1
4 5 6
9 8 7

입력이 5인 경우는 다음과 같이 출력한다.
5 4 3 2 1
6 7 8 9 10
15 14 13 12 11
16 17 18 19 20
25 24 23 22 21

입력이 n인 경우의 2차원 배열을 출력해보자.
'''
n = int(input())
lst = [[int(x) for x in range(1, n*n+1)][i:i+n] for i in range(0, n*n, n)]

for i in range(n):
    if((i+1)%2!=0):
        for j in range(n):
            lst[i] = sorted(lst[i], reverse=True)
            print(lst[i][j], end=" ")
        print()
    else:
        for j in range(n):
            print(lst[i][j], end=" ")
        print()