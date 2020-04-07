'''
1905 : (재귀함수) 1부터 n까지 합 구하기
정수 n이 입력으로 들어오면 1부터 n까지의 합을 구하시오.
'''
import sys
sys.setrecursionlimit(10**8)

def f(n):
    global sum
    global cnt

    if(cnt<=n):
        sum = sum + cnt
        cnt = cnt + 1
        f(n)

    return sum

n = int(input())
cnt = 1
sum = 0
print(f(n))