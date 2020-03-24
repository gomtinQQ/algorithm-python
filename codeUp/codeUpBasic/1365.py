'''
1365 : 사각형 출력하기 3
역시 별로 사각형을 출력하는 문제이다.
하지만 여기서는 대각선을 출력해야한다.
프로그램은 다음과 같이 진행된다.
1. n이 입력된다.(3<=n<=100)
2.대각선이 포함된 n*n사각형을 출력한다.
n = 9
*********
**     **
* *   * *
*  * *  *
*   *   *
*  * *  *
* *   * *
**     **
*********
'''
import math
n = int(input())
half = math.ceil(n/2)

for i in range(n):
    # 1, n 줄은 모두 별 출력
    if(i==0 or i==n-1):
        for j in range(n):
            print("*", end="")
    else:
        for j in range(n):
            if(j==0 or j==n-1):
                print("*", end="")
            elif(i==j or (j+i==n-1)):
                print("*", end="")
            else:
                print(" ", end="")
    print()
