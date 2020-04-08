'''
1920 : (재귀함수) 2진수 변환
어떤 10진수 n이 주어지면 2진수로 변환해서 출력하시오.
예)
10    ----->  1010
0    ----->  0
1    ----->  1
2    ----->  10
1024    ----->  10000000000
'''
import math
def f(n):
    if(n==0):
        print(0, end="")
    elif(n==1):
        print(1, end="")
    else:
        f(math.floor(n/2))
        print(n%2, end="")

n = int(input())
f(n)