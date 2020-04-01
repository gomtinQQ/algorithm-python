'''
1470 : [기초-배열연습] 2차원 배열 지그재그 채우기 2-3
다음과 같은 n*n 배열 구조를 출력해보자.

입력이 3인 경우 다음과 같이 출력한다.
1 6 7
2 5 8
3 4 9

입력이 5인 경우는 다음과 같이 출력한다.
1 10 11 20 21
2 9 12 19 22
3 8 13 18 23
4 7 14 17 24
5 6 15 16 25

입력이 n인 경우의 2차원 배열을 출력해보자.
'''
import numpy as np
n = int(input())
lst = [[int(x) for x in range(1, n*n+1)][i:i+n] for i in range(0, n*n, n)]

for i in range(n):
    if((i+1)%2==0):
        lst[i] = sorted(lst[i], reverse=True)

A = np.array(lst)
AT = A.T # Transpose(전치행렬)
for i in range(n):
    for j in range(n):
        print(AT[i][j], end=" ")
    print()
