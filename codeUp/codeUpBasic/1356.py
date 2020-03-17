'''
1356 : 사각형 출력하기 2
길이 n이 입력되면 다음과 같은 사각형을 출력한다.

예)n이 5일때
*****
*   *
*   *
*   *
*****
'''
n = int(input())
for i in range(1, n+1):
    if(i==1 or i==n):
        for j in range(0,n):
            print("*", end="")
    else:
        print("*", end="")
        for j in range(0, n-2):
            print(" ", end="")
        print("*", end="")
    print(" ")