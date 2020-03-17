'''
1357 : 삼각형 출력하기 4
n이 입력되면 다음 삼각형을 출력하시오.

예) n = 4
*
**
***
****
***
**
*
'''
n = int(input())
for i in range(1, n):
    for j in range(i):
        print("*", end="")
    print()

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


