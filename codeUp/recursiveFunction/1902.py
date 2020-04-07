'''
1902 : (재귀 함수) 1부터 n까지 역순으로 출력하기
정수 n부터 1까지 출력하는 재귀함수를 설계하시오.
'''
def f(n):
    if(n!=0):
        print(n)
        f(n-1)
    else:
        return

n = int(input())
global xn
f(n)
