'''
1371 : 마름모 출력하기
이번엔 마름모를 출력해보자.
n이 입력되면 대각선 2개의 길이가 2n인 마름모를 출력하시오.
6 4/**
7 3/*/2/*
8 2/*/4/*
9 1/*/6/*
10 0/*/8/*

    **
   *  *
  *    *
 *      *
*        *
*        *
 *      *
  *    *
   *  *
    **
'''
n = int(input())

# 윗 부분 출력
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(1):
        print("*", end="")
        print(" "*((i-1)*2), end="")
    print("*")

# 아랫 부분 출력
for i in range(1, n+1):
    for j in range(n-1, n-i, -1):
        print(" ", end="")
    for j in range(1):
        print("*", end="")
    for j in range(n-i, 0, -1):
        print(" "*(2), end="")
    print("*")


