'''
1538 : [기초-함수작성] 함수로 odd 또는 even 출력하기
홀수가 입력되면 odd, 짝수가 입력되면 even을 출력한다.
단, 함수형 문제이므로 함수 f()만 작성하시오.
'''
def f(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")

n = int(input())
f(n)
