'''
1354 : 삼각형 출력하기 2
길이 n이 입력되면 역삼각형을 출력한다.

예) n이 5이면
*****
****
***
**
*
'''
n = int(input())
for i in range(n, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print("")