'''
1473 : [기초-배열연습] 2차원 배열 지그재그 채우기 2-6
다음과 같은 n*m 배열 구조를 출력해보자.

입력이 3 4인 경우 다음과 같이 출력한다.
9 10 11 12
8 7 6 5
1 2 3 4

입력이 4 5인 경우는 다음과 같이 출력한다.
20 19 18 17 16
11 12 13 14 15
10 9 8 7 6
1 2 3 4 5

입력이 n m인 경우의 2차원 배열을 출력해보자.
'''
n, m = input().split()
n = int(n)
m = int(m)
lst = [[int(x) for x in range(1, n*m+1)][i:i+m] for i in range(0, n*m, m)]

for i in range(n-1, -1, -1):
    if((i+1)%2==0):
        lst[i] = sorted(lst[i], reverse=True)
        for j in range(m):
            print(lst[i][j], end=" ")
        print()
    else:
        for j in range(m):
            print(lst[i][j], end=" ")
        print()