'''
1474 : [기초-배열연습] 2차원 배열 지그재그 채우기 2-7
다음과 같은 n*m 배열 구조를 출력해보자.

입력이 3 4인 경우 다음과 같이 출력한다.
10 9 4 3
11 8 5 2
12 7 6 1

입력이 4 5인 경우는 다음과 같이 출력한다.
20 13 12 5 4
19 14 11 6 3
18 15 10 7 2
17 16 9 8 1

입력이 n m인 경우의 2차원 배열을 출력해보자.
'''
import numpy as np
n, m = input().split()
n = int(n)
m = int(m)
lst = [[x for x in range(1, n*m+1)][i:i+n] for i in range(0, n*m, n)]

for i in range(m):
    if((i+1)%2!=0):
        lst[i] = sorted(lst[i], reverse=True)

A = np.array(lst)
AT = A.T

for i in range(n):
    for j in range(m-1, -1, -1):
        print(AT[i][j], end=" ")
    print()
