'''
1904 : (재귀함수) 두 수 사이의 홀수 출력하기
시작수(a)와 마지막 수(b)가 입력되면
a부터 b까지의 모든 홀수를 출력하시오.
'''
def f(a, b):
    if(a>b):
        return
    elif(a%2!=0):
        print(a, end=" ")
        a = a+1
        f(a, b)
    else:
        a = a+1
        f(a, b)

a, b = input().split()
a = int(a)
b = int(b)
f(a,b)