'''
1366 : 사각형 출력하기 4
사각형의 크기 n이 입력된다.(n은 홀수)
대각선과 테두리가 그려진 사각형에 가로, 세로 중심에 선을 추가한 사각형을 출력한다.
n = 17
*****************
**      *      **
* *     *     * *
*  *    *    *  *
*   *   *   *   *
*    *  *  *    *
*     * * *     *
*      ***      *
*****************
*      ***      *
*     * * *     *
*    *  *  *    *
*   *   *   *   *
*  *    *    *  *
* *     *     * *
**      *      **
*****************

n = int(input())
mid = int(n/2)

for i in range(n+1):
    # 1, mid, n은 모두 별 출력
    if(i==0 or i==(n) or i==(mid)):
        for j in range(n):
            print("*", end="")
    else:
        for j in range(n):
            if(j==0 or j==(n-1) or j==(mid)):
                print("*", end="")
            elif(j<mid):
                if(j==i):
                    print("*", end="")
                else:
                    print(" ", end="")
            elif(j>mid):
                if(j==(n-i-1)):
                    print("*", end="")
                else:
                    print(" ", end="")
    print()
'''
n = int(input())
mid = int(n/2)

for i in range(n):
    # 1, mid, n은 모두 별 출력
    if(i==0 or i==(n-1) or i==(mid)):
        for j in range(n):
            print("*", end="")
    else:
        for j in range(n):
            if(j==0 or j==(n-1) or j==(mid)):
                print("*", end="")
            elif((j<mid and i<mid) or (j>mid and i>mid)):
                if(j==i):
                    print("*", end="")
                else:
                    print(" ", end="")
            elif((j>mid and i<mid) or (j<mid and i>mid)):
                if(j==(n-i-1)):
                    print("*", end="")
                else:
                    print(" ", end="")
    print()