'''
1355 : 삼각형 출력하기 3
길이 n이 입력되면 다음과 같은 역삼각형을 출력한다.

예)n이 5이면
*****
 ****
  ***
   **
    *
'''
n = int(input())
for i in range(n, 0, -1):
    for j in range(0, n-i):
        print(" ", end="")
    for j in range(0, i):
        print("*", end="")
    print("")
