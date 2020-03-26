'''
1369 : 빗금 친 사각형 출력하기
별모양 출력하기에 재미를 붙인 admin은 이번에는 빗금 친 사각형을 출력하기로 했다.
n*n 사각형에서 k간격만큼 빗금을 그어 출력하는 프로그램을 작성하시오.
예) n=10, k=3이면,

**********
**  *  * *
*  *  *  *
* *  *  **
**  *  * *
*  *  *  *
* *  *  **
**  *  * *
*  *  *  *
**********
'''
n, k = input().split()
n = int(n)
k = int(k)

for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or i==n):
            print("*", end="")
        elif(j==1 or j==n):
            print("*", end="")
        elif((i+j-1)%k==0):
            print("*", end="")
        else:
            print(" ", end="")
    print()