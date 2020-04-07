'''
1901 : (재귀 함수) 1부터 n까지 출력하기
1부터 정수 n까지 출력하는 재귀함수를 설계하시오.
'''
def f(n):
    global cnt
    if(cnt!=n+1):
        print(cnt)
        cnt = cnt+1
        f(n)
    else:
        return

cnt = 1
n = int(input())
f(n)